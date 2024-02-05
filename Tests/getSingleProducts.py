import requests

url = "https://fakestoreapi.com/products/15"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)