import grpc
import os
from proto import messages_pb2_grpc,messages_pb2

port = os.environ.get('PORT') or 50051

def run():
    with grpc.insecure_channel(f"127.0.0.1:{port}") as channel:
        hello_stub = messages_pb2_grpc.HelloStub(channel)
        hello_request = messages_pb2_grpc.proto_dot_messages__pb2.HelloRequest(message="python怎么入门")
        response = hello_stub.sayHello(hello_request)
        print(response)
        print(response.message)
        
def hello(msg:str)->str:
    # 使用 host.docker.internal指代宿主机的ip
    with grpc.insecure_channel(f"host.docker.internal:{port}") as channel:
        hello_stub = messages_pb2_grpc.HelloStub(channel)
        hello_request = messages_pb2_grpc.proto_dot_messages__pb2.HelloRequest(message=msg)
        response = hello_stub.sayHello(hello_request)
        return response.message

if __name__ == "__main__":
    run()