import requests
import json

r = requests.get('https://api.github.com/events')

events = json.loads(r.text)

for event in events:
    print(event.get("repo").get("url"))