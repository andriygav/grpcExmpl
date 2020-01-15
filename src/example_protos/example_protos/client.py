# coding=utf-8
import argparse

import time

import grpc

from .example_pb2 import Request, Response, DataResponseField
from .example_pb2_grpc import ExampleServiceStub

MAX_MSG_LENGTH = 30 * 1024 * 1024

class ExampleClient(object):
    def __init__(self, address='localhost:9878'):
        self.address = address
        self.channel = grpc.insecure_channel(address, options=[('grpc.max_send_message_length', MAX_MSG_LENGTH),
                                                              ('grpc.max_message_length', MAX_MSG_LENGTH),
                                                              ('grpc.max_receive_message_length', MAX_MSG_LENGTH)])
        self.stub = ExampleServiceStub(self.channel)
        pass

    def GetDate(self, a=0, b=1, types='sum', timeout=None, address=None):
        request = Request(A=int(a),
                        B=int(b),
                          Type=str(types))

        response = self.stub.GetData.future(request).result(timeout)

        result = dict()
        result[types] = response.Result.Value
        return result

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument('a', help='first value')
    parser.add_argument('b', help='second value')
    parser.add_argument('--type', default = 'sum', help='extion type', choices=['sum', 'prod'])
    parser.add_argument('--server', default = 'localhost:9878', help='server host')
    namespace = parser.parse_args()
    argv = vars(namespace)
    
    client = ExampleClient(argv['server'])

    s = time.time()
    result = client.GetDate(int(argv['a']), int(argv['b']), argv['type'])
    total_time = time.time() - s

    print('answer: {}={}'.format(argv['type'], result[argv['type']]))
    print('time: {}'.format(total_time))

if __name__ == '__main__':
    start()