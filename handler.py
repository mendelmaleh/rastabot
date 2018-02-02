import os
import json
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

token = os.environ['TELEGRAM_TOKEN']
baseURL = "https://api.telegram.org/bot{}".format(token)
admins = [425478612]
ver = "1.0.0.6"

# def unloader(event):
#     data = json.loads(event["body"])
#     message = str(data["message"]["text"])
#     chatID = data["message"]["chat"]["id"]
#     username = data["message"]["chat"]["username"]
#     firstname = data["message"]["chat"]["first_name"]
#     answer = "@{}, I'm not sure what you did...".format(username)
#     return data, chatID, username, firstname, answer


# def isList(i, l):
#     if i in l:
#         return True
#     else:
#         return False

def stamptohuman(t):
    s = t % 60
    m = ((t - s) / 60) % 60
    h = ((t - ((m * 60) + s)) / 3600) % 24
    return [int(h), int(m), int(s)]


def encoder(ans, chat_id, base_url):
    data = {"text": ans.encode("utf8"), "chat_id": chat_id}
    url = base_url + "/sendMessage"
    requests.post(url, data)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chatID = data["message"]["chat"]["id"]
        firstname = data["message"]["chat"]["first_name"]
        time = stamptohuman(data["message"]["date"])

        try:
            username = "@" + data["message"]["chat"]["username"]
        except:
            username = firstname

        saved = {"ver": ver, "/start": "Hi {}".format(username), "time": "{}:{}:{}".format(time[0], time[1], time[2]), "data": str(data)}

        answer = "{}, I'm not sure what you want...".format(username)

        # admin = islist(chatID, admins)

        if message in saved:
            answer = saved[message]
        elif message[0].isupper():
            lowermsg = message.lower()
            if lowermsg in saved:
                answer = saved[lowermsg]

        encoder(answer, chatID, baseURL)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
