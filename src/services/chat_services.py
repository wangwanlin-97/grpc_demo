from proto import messages_pb2_grpc
from proto.messages_pb2 import ChatResponse
from spark_api.auth import Asker
class ChatService(messages_pb2_grpc.ChatServicer):
    
    def chat(self,iter_request,context):
        # fd = "812141"
        # gtToken = "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"
        # cookie = "JSESSIONID=957103AB7568F0CD35ED590100361AA3; di_c_mti=6a336c50-d424-6070-8870-ce0b0d3bd720; d_d_app_ver=1.4.0; d_d_ci=b0dd94d2-5aa9-60a4-a52b-68c38cf3d953; ssoSessionId=9f2413a1-64da-42fe-955a-853107cfd4c2; account_id=17463189936; daas_st={%22sdk_ver%22:%221.3.9%22%2C%22status%22:%220%22}; appid=150b4dfebe; gt_local_id=9DSKcsXgtCC2u0ObpRx5qQUq4o6N1848lpLTwJk4avHd2a1UuNMIwA=="

        # from spark_desk.core import SparkWeb
    
        # sparkWeb = SparkWeb(cookie=cookie, fd=fd, GtToken=gtToken)
        print(context.peer())
        for request in iter_request:
            # fd, GtToken,cookie 已经失效，需要重新获取
            # chat_ans = sparkWeb.chat(request.message)
            # for ans in chat_ans:
            #     response = ChatResponse(message=ans)
            #     yield response
            asker = Asker()
            response_message = asker.askGpt(request.message)
            response = ChatResponse(message=response_message)
            yield response