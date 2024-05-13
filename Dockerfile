FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip3 config set install.trusted-host pypi.tuna.tsinghua.edu.cn

RUN pip3 install grpcio

RUN pip3 install grpcio-tools

RUN pip3 install protobuf

RUN pip3 install websocket-client

ENV PYTHONPATH ./src

ENTRYPOINT ["python3", "./src/server/hello_server.py"]
