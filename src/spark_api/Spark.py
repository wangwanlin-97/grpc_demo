from datetime import datetime
from time import mktime
import pytz
import configparser
from wsgiref.handlers import format_date_time
import hmac
import hashlib
import base64
from socket import socket
import websocket
import _thread as thread
import ssl
import json
from urllib.parse import quote
from urllib.parse import urlencode


class SparkClient:
    def __init__(self, model: str, appId: str, apiScrect: str, apiKey: str):
        self.model_version = model
        self.appId = appId
        self.apiScrect = apiScrect
        self.apiKey = apiKey

    def get_auth_url(self):
        cur_time = datetime.now()
        date = format_date_time(mktime(cur_time.timetuple()))

        if self.model_version == "v1.5":
            url_version = "v1.1"
        elif self.model_version == "v2.1":
            url_version = "v2.1"
        elif self.model_version == "v3.1":
            url_version = "v3.1"
        elif self.model_version == "v3.5":
            url_version = "v3.5"

        tmp = "host: " + "spark-api.xf-yun.com" + "\n"
        tmp += "date: " + date + "\n"
        tmp += "GET " + f"/{url_version}/chat" + " HTTP/1.1"

        APISecret = self.apiScrect
        APIKey = self.apiKey
        tmp_sha = hmac.new(
            APISecret.encode("utf-8"), tmp.encode("utf-8"), digestmod=hashlib.sha256
        ).digest()

        signature = base64.b64encode(tmp_sha).decode(encoding="utf-8")
        authorization_origin = f"api_key='{APIKey}', algorithm='hmac-sha256', headers='host date request-line', signature='{signature}'"
        authorization_origin = authorization_origin.replace("'", '"')
        authorization = base64.b64encode(authorization_origin.encode("utf-8")).decode(
            encoding="utf-8"
        )

        v = {
            "authorization": authorization,  # 上方鉴权生成的authorization
            "date": date,  # 步骤1生成的date
            "host": "spark-api.xf-yun.com",  # 请求的主机名，根据具体接口替换
        }
        url = f"wss://spark-api.xf-yun.com/{url_version}/chat?" + urlencode(v)
        return url

    def get_request(self, question: str):
        versions = {
            "v1.5": "general",
            "v2.1": "generalv2",
            "v3.1": "generalv3",
            "v3.5": "generalv3.5",
        }
        request = {
            "header": {"app_id": self.appId, "uid": "12345"},
            "parameter": {
                "chat": {
                    "domain": versions.get(self.model_version),
                    "temperature": 0.5,
                    "max_tokens": 1024,
                }
            },
            "payload": {
                "message": {
                    "text": [
                        # {
                        #     "role": "system",
                        #     "content": "你现在扮演李白，你豪情万丈，狂放不羁；接下来请用李白的口吻和用户对话。",
                        # },  # 设置对话背景或者模型角色
                        # {"role": "user", "content": "你是谁"},  # 用户的历史问题
                        # {"role": "assistant", "content": "....."},  # AI的历史回答结果
                        # # ....... 省略的历史对话
                        {
                            "role": "user",
                            "content": question,
                        },  # 最新的一条问题，如无需上下文，可只传最新一条问题
                    ]
                }
            },
        }
        return request


class Asker:
    res = ""
    
    def __init__(self):
        config = configparser.ConfigParser()
        self.res = ""
        config.read("config.ini")
        appid = config.get("SPARK_API", "APPID")
        APIkey = config.get("SPARK_API", "API_KEY")
        APIscrect = config.get("SPARK_API", "API_SECRET")
        self.sp = SparkClient(
            model="v2.1",
            appId=appid,
            apiKey=APIkey,
            apiScrect=APIscrect,
        )
    def askGpt(self,message: str):
        
        request = self.sp.get_request(message)

        def on_open(ws):
            ws.send(json.dumps(request))

        def on_close(ws, b, c):
            ...

        def on_error(ws, error):
            print("### error:", error)

        def on_message(ws, message):
            data = json.loads(message)
            code = data["header"]["code"]
            if code != 0:
                ws.close()
            else:
                choices = data["payload"]["choices"]
                status = choices["status"]
                content = choices["text"][0]["content"]
                print(content,end="")
                self.res+=content
                if status == 2:
                    ws.close()

        ws = websocket.WebSocketApp(
        self.sp.get_auth_url(),
        on_open=on_open,
        on_message=on_message,
        on_close=on_close,
        on_error=on_error,
    )

        ws.run_forever()
        return self.res
