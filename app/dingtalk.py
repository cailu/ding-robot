import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import config
import requests


class DingTalk(object):
    SIGN_SECRET = os.environ.get(config.DING_ROBOT_SIGN_SECRET)
    BASE_URL = os.environ.get(config.DING_ROBOT_URL)

    def call(self, msg):
        url = self.gen_url()
        data = self.gen_text_data(msg)
        requests.post(url, json=data)

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