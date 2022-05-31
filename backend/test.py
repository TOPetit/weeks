import requests
import json

BASE_URL = "http://127.0.0.1:5000/"

headers = {"Content-type": "application/json"}

res = requests.post(BASE_URL + "register", json.dumps({"email": "", "password": "12345"}), headers=headers)

print(str(res.status_code) + ': ' + res.text)