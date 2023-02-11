import os
import json
import requests
from config import config


class OpenAI(object):
    APP_KEY = os.environ.get(config.OPENAI_APP_KEY)

    @staticmethod
    def call(tips):
        url = 'https://api.openai.com/v1/completions'
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + OpenAI.APP_KEY
        }
        data = dict(
            model="text-davinci-003",
            prompt=tips,
            temperature=0.6,
            stream=False,
            max_tokens=1024,
            top_p=1,
            n=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        resp = requests.post(url, headers=headers, json=data)
        return resp.json()['choices'][0]['text']

    @staticmethod
    def parse(text):
        tokens = []
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                continue
            if line.startswith("data: [DONE]"):
                break
            if line.startswith("data: "):
                value = json.loads(line[6:])
                tk = value['choices'][0]['text']
                tokens.append(tk)
        return ''.join(tokens)


if __name__ == '__main__':
    prompt = "光速是恒定的么"
    print(prompt)
    data = OpenAI.call(prompt)
    print(data)
