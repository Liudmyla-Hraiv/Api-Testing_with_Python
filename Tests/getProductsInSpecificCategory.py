import requests

url = "https://fakestoreapi.com/products/category/women's clothing"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
