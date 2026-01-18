import requests
import json

payload = {
  "name": "string",
  "price": 0,
  "in_stock": True
}
requestUrl = "http://192.168.45.167:8000/items"
response = requests.post(requestUrl,data=payload)

print(response.content)
print(requests.get("http://192.168.45.167:8000/items").text)