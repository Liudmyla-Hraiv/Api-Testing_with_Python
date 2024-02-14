import pytest
import requests
import json

base_url = "https://fakestoreapi.com"

def test_getToken():
    payload = json.dumps({
    "username": "mor_2314",
    "password": "83r5^_"
    })
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.post(url= base_url + '/auth/login', headers=headers, data=payload)
 
    assert 200 == response.status_code
    print(response.status_code)