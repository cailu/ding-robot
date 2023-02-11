import random

messages = ["我太弱了", "我真的太弱了", "我弱。。。", "我菜鸡一个，别找我聊天了", "真的，我是弱鸡。。。"]


def get_one_msg():
    return random.choice(messages)
