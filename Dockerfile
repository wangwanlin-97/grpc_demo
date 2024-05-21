FROM python:3.10-slim

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/

RUN pip3 config set install.trusted-host pypi.tuna.tsinghua.edu.cn

# RUN pip3 install grpcio

# RUN pip3 install grpcio-tools

# RUN pip3 install protobuf

# RUN pip3 install websocket-client
RUN pip3 install -r ./requirements.txt

# ENV PYTHONPATH .

CMD ["python3", "src/server/hello_server.py"]
