import pytest
import requests

base_url = "https://fakestoreapi.com"
def test_limitReq():
    header = {
        'Content-Type' : 'application/json'
    }
    response = requests.get(url= base_url + '/products?limit=5', headers=header)
 
    assert 200 == response.status_code
    print(response.status_code)
