import pytest
import requests

base_url = "https://fakestoreapi.com"

def test_getOneProduct():
    headers = {
        'Content-Type' : 'application/json'
    }
    
    response = requests.get(url= base_url + '/products/13', headers=headers)
 
    assert 200 == response.status_code
    print(response.status_code)