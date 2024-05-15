FROM python:3.10.14-alpine

WORKDIR /app

COPY . /app

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip3 config set install.trusted-host pypi.tuna.tsinghua.edu.cn

RUN pip3 install grpcio

RUN pip3 install grpcio-tools

RUN pip3 install protobuf

RUN pip3 install websocket-client

ENV PYTHONPATH /app

CMD ["python3", "./server/hello_server.py"]
