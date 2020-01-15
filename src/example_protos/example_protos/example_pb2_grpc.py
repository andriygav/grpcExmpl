# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from example_protos import example_pb2 as example__protos_dot_example__pb2


class ExampleServiceStub(object):
  """Служба извлечения
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetData = channel.unary_unary(
        '/example.v1.ExampleService/GetData',
        request_serializer=example__protos_dot_example__pb2.Request.SerializeToString,
        response_deserializer=example__protos_dot_example__pb2.Response.FromString,
        )


class ExampleServiceServicer(object):
  """Служба извлечения
  """

  def GetData(self, request, context):
    """Запрос на получение
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ExampleServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetData': grpc.unary_unary_rpc_method_handler(
          servicer.GetData,
          request_deserializer=example__protos_dot_example__pb2.Request.FromString,
          response_serializer=example__protos_dot_example__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'example.v1.ExampleService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))