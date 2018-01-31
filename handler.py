import json
import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests
import ast

token = "516160274:AAEgyfeASRRdb0_XFDxtAOTtxQsjJjkt1bo"
baseURL = "https://api.telegram.org/bot{}".format(token)
admins = [425478612]
words = ["start"]


def isList(uid, aList):
    if uid in aList:
        return True
    else:
        return False


def canEval(i):
    try:
        ast.literal_eval(i)
        return True
    except (NameError, ValueError):
        return False


def hello(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]

        ans = {"/start": ("Hello {}".format(first_name))}
        admin = isList(chat_id, admins)
        response = "Please /start, {}".format(first_name)

        if message in ans:
            response = str(ans[message])

        elif admin is True & canEval(message) is True:
            response = str(ast.literal_(message))

        elif admin is True & canEval(message) is False:
            response = "{} is not a word".format(message)

        elif admin is False:
            response = "Use /help"

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = baseURL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
