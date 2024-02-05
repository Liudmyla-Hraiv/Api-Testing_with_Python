import requests

url = "https://fakestoreapi.com/products?limit=5"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
