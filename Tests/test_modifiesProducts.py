import pytest
import requests
import json

base_url = "https://fakestoreapi.com"

def test_modify():
    payload = json.dumps({
    "title": "Generic Metal Table",
    "price": 28.33,
    "description": "lorem ipsum set",
    "category": "women's clothing",
    "image": "http://placeimg.com/640/480/fashion"
})
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.put(url= base_url + '/products/7', headers=headers, data=payload)
 
    assert 200 == response.status_code
    print(response.status_code)