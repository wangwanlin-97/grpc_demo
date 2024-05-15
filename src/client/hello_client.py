import grpc
from proto import messages_pb2_grpc,messages_pb2

def run():
    with grpc.insecure_channel("119.3.37.42:50051") as channel:
        hello_stub = messages_pb2_grpc.HelloStub(channel)
        hello_request = messages_pb2_grpc.proto_dot_messages__pb2.HelloRequest(message="python怎么入门")
        response = hello_stub.sayHello(hello_request)
        print(response)
        print(response.message)

if __name__ == "__main__":
    run()