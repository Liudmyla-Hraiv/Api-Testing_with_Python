import requests
import json

url = "https://fakestoreapi.com/auth/login"

payload = json.dumps({
    "username": "mor_2314",
    "password": "83r5^_"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
