from proto import messages_pb2_grpc

class HelloService(messages_pb2_grpc.HelloServicer):
    def __init__(self):
        pass
    
    def sayHello(self, request, context):
        result = messages_pb2_grpc.proto_dot_messages__pb2.HelloReply(message=f"{request.name} hello aaaaa")
        return result