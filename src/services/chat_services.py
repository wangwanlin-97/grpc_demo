from proto import messages_pb2_grpc
from proto.messages_pb2 import ChatResponse

class ChatService(messages_pb2_grpc.ChatServicer):
    
    def chat(self,iter_request,context):
        print(context.peer())
        for request in iter_request:
            response = ChatResponse(message=f"{request.message} received")
            yield response