import requests
import json

r = requests.get('https://api.github.com/events')
print(r.text)
print(json.loads)