import requests
import json

url = "https://fakestoreapi.com/products/7"

payload = json.dumps({
    "title": "Generic Metal Table",
    "price": 28.33,
    "description": "lorem ipsum set",
    "category": "women's clothing",
    "image": "http://placeimg.com/640/480/fashion"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
