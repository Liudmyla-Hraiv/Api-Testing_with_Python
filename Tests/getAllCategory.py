import requests

url = "https://fakestoreapi.com/products/categories"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
