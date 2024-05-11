FROM alpine:3.18

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "./src/server/hello_server.py"]
