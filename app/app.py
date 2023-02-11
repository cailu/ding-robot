import uuid
import flask
from config import config
from dingtalk.dingtalk import DingTalk

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    return uuid.uuid4().hex


@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    header = flask.request.headers
    data = flask.request.get_json()
    if not DingTalk.check_token(header):
        return 'failed'
    msg = DingTalk.get_msg(data)
    DingTalk.call("好啊好啊, " + msg)


if __name__ == '__main__':
    config.check_config()
    app.run(host='0.0.0.0', port=5000)

