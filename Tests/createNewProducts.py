import requests
import json

url = "https://fakestoreapi.com/products"

payload = json.dumps({
    "title": "Tasty Cotton Table",
    "price": 40.99,
    "description": "lorem ipsum set",
    "category": "women's clothing",
    "image": "http://placeimg.com/640/480/fashion"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
