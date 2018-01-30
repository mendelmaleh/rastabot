import json
import os
import sys

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

token = "516160274:AAEgyfeASRRdb0_XFDxtAOTtxQsjJjkt1bo"
baseURL = "https://api.telegram.org/bot{}".format(token)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]
        first_name = data["message"]["chat"]["first_name"]

        response = "Please /start, {}".format(first_name)

        if "start" in message:
            response = "Hello {}".format(first_name)
        elif "event" in message:
            response = str(event)
        elif "data" in message:
            response = str(data)
        elif "/event" in message:
            response = "--forward slash\n\n" + str(event)
        elif "/data" in message:
            response = "--forward slash\n\n" + str(data)

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = baseURL + "/sendMessage"
        requests.post(url, data)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
