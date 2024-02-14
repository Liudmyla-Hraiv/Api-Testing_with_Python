import pytest
import requests
import json

base_url = "https://fakestoreapi.com"
def test_createProduct() :
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
    response = requests.post(url= base_url + '/products', headers=headers, data=payload)
    assert 200 == response.status_code
    print(response.status_code)
