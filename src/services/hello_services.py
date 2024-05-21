from proto import messages_pb2_grpc
from spark_api.Spark import Asker
from proto.messages_pb2 import HelloReply


class HelloService(messages_pb2_grpc.HelloServicer):
    def __init__(self):
        pass

    def sayHello(self, request, context):

        asker = Asker()
        response_message = asker.askGpt(request.message)
        result = messages_pb2_grpc.proto_dot_messages__pb2.HelloReply(
            message=response_message, context=context
        )
        return result
