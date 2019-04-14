import requests
import json

slack_post_url = "https://hooks.slack.com/services/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"
name = "python_taro"
text = "testyade"

requests.post(
    slack_post_url,
    data=json.dumps(
        {"text": text,
         "username": name,
         "icon_emoji": ":python:"}))
