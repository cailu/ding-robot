import os

DING_ROBOT_SIGN_SECRET = 'DING_ROBOT_SIGN_SECRET'
DING_ROBOT_URL = 'DING_ROBOT_URL'
DING_TOKEN = 'DING_TOKEN'
OPENAI_APP_KEY = 'OPENAI_APP_KEY'

CONFIG_KEY_LIST = [DING_ROBOT_URL, DING_ROBOT_SIGN_SECRET, DING_TOKEN, OPENAI_APP_KEY]


def check_config():
    for key in CONFIG_KEY_LIST:
        if key not in os.environ:
            raise Exception("Could not found setting {}".format(key))


if __name__ == '__main__':
    check_config()