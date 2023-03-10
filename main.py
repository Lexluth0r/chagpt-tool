import json
from revChatGPT.V1 import Chatbot
from flask import Flask, request, render_template,jsonify, redirect

server = Flask(__name__)

# get config
with open("config.json", "r") as f: config = json.load(f)

# init chatbot
chatbot = Chatbot(config)

def generate_response(prompt):
    response = ""
    for data in chatbot.ask(prompt):
        response = data["message"]
    return response


@server.route("/api/chat",methods=['POST'])
def get_chat_bot_response():
    resp = {'code':200,'msg':'','data':{}}
    req = json.loads(request.data.decode('utf-8'))
    q = req['question']
    resp['data']['answer'] = generate_response(q)
    return jsonify(resp)

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
