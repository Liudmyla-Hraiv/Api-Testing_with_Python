import requests

url = "https://fakestoreapi.com/products/15"

payload = ""
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
