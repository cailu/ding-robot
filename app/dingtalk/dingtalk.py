import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
from app.config import config


class DingTalk(object):
    SIGN_SECRET = os.environ.get(config.DING_ROBOT_SIGN_SECRET)
    BASE_URL = os.environ.get(config.DING_ROBOT_URL)
    TOKEN = os.environ.get(config.DING_TOKEN)

    @staticmethod
    def call(msg):
        url = DingTalk.gen_url()
        data = DingTalk.gen_text_data(msg)
        requests.post(url, json=data)

    @staticmethod
    def check_token(header):
        token = header.get('Token')
        return DingTalk.TOKEN == token

    @staticmethod
    def get_msg(data):
        return data.get('text', {}).get('content')

    @staticmethod
    def gen_text_data(msg):
        return {
            "text": {
                "content": msg,
            },
            "msgtype": "text"
        }

    @staticmethod
    def gen_url():
        timestamp = str(round(time.time() * 1000))
        sign = DingTalk.gen_sign(timestamp)
        url = DingTalk.BASE_URL + '&timestamp={}&sign={}'.format(timestamp, sign)
        return url

    @staticmethod
    def gen_sign(timestamp):
        secret = DingTalk.SIGN_SECRET
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return sign


if __name__ == '__main__':
    dingClient = DingTalk()
    dingClient.call("test")