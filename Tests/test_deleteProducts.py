import pytest
import requests

base_url = "https://fakestoreapi.com"

def test_deleteReq():
    headers = {
        'Content-Type' : 'application/json'
    }
    response = requests.delete(url= base_url + '/products/15', headers=headers)
 
    assert 200 == response.status_code
    print(response.status_code)