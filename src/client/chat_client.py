import grpc
from proto import messages_pb2_grpc
from proto.messages_pb2 import ChatRequest

def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        chat_stub = messages_pb2_grpc.ChatStub(channel)
        while True:
            q=input("user:")
            response = chat_stub.chat(iter([ChatRequest(message=q,name="wang")]),timeout=1)
            for message in response:
                print(f"REPLY:{message.message}\n")

if __name__ == "__main__":
    run()