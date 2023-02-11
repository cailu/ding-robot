import uuid
import flask

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST', 'HEAD'])
def home():
    return uuid.uuid4().hex


@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    header = flask.request.headers
    data = flask.request.get_json()
    print("header:", header)
    print("data:", data)
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

