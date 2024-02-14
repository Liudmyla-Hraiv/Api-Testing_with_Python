import pytest
import requests
import json

base_url = "https://fakestoreapi.com"
def test_update():
    payload = json.dumps({
    "title": "Handmade Concrete Bike",
    "price": 28.55
    })
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.patch(url= base_url + '/products/8', headers=headers, data=payload)
 
    assert 200 == response.status_code
    print(response.status_code)