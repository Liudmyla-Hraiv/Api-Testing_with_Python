import pytest
import requests

base_url = "https://fakestoreapi.com"

def test_sort():
    headers = {
        'Content-Type' : 'application/json'
    }

    response = requests.get(url= base_url + '/products?sort=desc', headers=headers)
 
    assert 200 == response.status_code
    print(response.status_code)