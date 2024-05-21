from flask import Flask,request
from flask_cors import CORS

from client.hello_client import hello

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=["POST"])
def ask():
    data = request.get_json()
    msg = data.get('msg')
    response = hello(msg)
    return {'response': response}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)