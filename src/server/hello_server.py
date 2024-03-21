from concurrent import futures
import grpc

from proto import messages_pb2_grpc
from services.hello_services import HelloService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    messages_pb2_grpc.add_HelloServicer_to_server(HelloService(),server)
    server.add_insecure_port("[::]:8888")
    server.start()
    print("Server is running")
    server.wait_for_termination()
    
if __name__ == "__main__":
    serve()