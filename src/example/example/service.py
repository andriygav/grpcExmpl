# coding=utf-8
import time
import logging  
from concurrent import futures
import argparse

import grpc
from grpc_reflection.v1alpha import reflection

from configobj import ConfigObj

from example_protos.example_pb2 import Request, Response, DataResponseField, DESCRIPTOR
from example_protos.example_pb2_grpc import ExampleServiceStub, add_ExampleServiceServicer_to_server, ExampleServiceServicer

from .prototype import init_model, extractor

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

MAX_MSG_LENGTH = 100 * 1024 * 1024

class ExampleService(ExampleServiceServicer):

    def GetData(self, request, context):
        a = int(request.A)
        b = int(request.B)
        types = request.Type
        logging.warning('request data: {}, {}, {}'.format(a, b, types))
        
        start_time = time.time()
        
        result = extractor(a, b, types)

        logging.warning('result: {}'.format(str(result)))
     
        response = Response(Result=DataResponseField(Value=result[types]))

        logging.warning('response data.')
        return response


def serve(config):
    logging.warning('loading data for model')
    init_model(config)

    server = grpc.server(
        futures.ThreadPoolExecutor(
            max_workers=int(config['service']['max workers'])
        ),
        options=[('grpc.max_send_message_length', MAX_MSG_LENGTH),
                 ('grpc.max_message_length', MAX_MSG_LENGTH),
                 ('grpc.max_receive_message_length', MAX_MSG_LENGTH)]
    )
    add_ExampleServiceServicer_to_server(ExampleService(), server)
    SERVICE_NAMES = (
        DESCRIPTOR.services_by_name['ExampleService'].full_name,
        reflection.SERVICE_NAME,
    )

    reflection.enable_server_reflection(SERVICE_NAMES, server)
    server.add_insecure_port(config['service']['port'])

    server.start()
    logging.warning("Server running on port {}".format(config['service']['port']))

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('config', help='path to the config file')
    namespace = parser.parse_args()
    argv = vars(namespace)

    config = ConfigObj(infile=argv['config'], encoding='utf-8')

    serve(config)


if __name__ == '__main__':
    start()


