import requests
import json

url = "https://fakestoreapi.com/products/8"

payload = json.dumps({
    "title": "Handmade Concrete Bike",
    "price": 28.55
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
