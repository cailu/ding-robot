import uuid
import flask
import redis

from config import config
from dingtalk.dingtalk import DingTalk
from chatgpt.chatgpt import OpenAI

app = flask.Flask(__name__)
ding = DingTalk()
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    return uuid.uuid4().hex


@app.route('/chatgpt', methods=['POST'])
def chat_gpt():
    header = flask.request.headers
    data = flask.request.get_json()
    if not ding.check_token(header):
        return 'failed'
    msg = ding.get_msg(data)
    value = r.get(msg)
    if not value:
        value = OpenAI.call(msg)
        r.set(msg, value)
    ding.call(value)


if __name__ == '__main__':
    config.check_config()
    app.run(host='0.0.0.0', port=5000)

