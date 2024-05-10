import grpc
from proto import messages_pb2_grpc,messages_pb2

def run():
    with grpc.insecure_channel("localhost:8888") as channel:
        hello_stub = messages_pb2_grpc.HelloStub(channel)
        hello_request = messages_pb2_grpc.proto_dot_messages__pb2.HelloRequest(message="怎么减肚子")
        response = hello_stub.sayHello(hello_request)
        print(response.message)

if __name__ == "__main__":
    run()