import pytest
import requests

base_url = "https://fakestoreapi.com"

def test_getOneCategoty():
    header = {
        'Content-Type' : 'application/json'
    }
    response = requests.get(url= base_url + '/products/category/women\'s clothing', headers=header)
 
    assert 200 == response.status_code
    print(response.status_code)
