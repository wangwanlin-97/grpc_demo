from concurrent import futures
import grpc

from proto import messages_pb2_grpc
from services.chat_services import ChatService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    messages_pb2_grpc.add_ChatServicer_to_server(ChatService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("chat server is running")
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()