import grpc
from proto import messages_pb2_grpc
from proto.messages_pb2 import ChatRequest
from configparser import ConfigParser
import sys

def run():   
    with grpc.insecure_channel("localhost:50051") as channel:
        chat_stub = messages_pb2_grpc.ChatStub(channel)
        while True:
            q=input("\nuser:")
            response = chat_stub.chat(iter([ChatRequest(message=q,name="wang")]))
            print("REPLY:")
            for message in response:
                sys.stdout.flush()
                print(f"{message.message}",end="")
                

if __name__ == "__main__":
    run()