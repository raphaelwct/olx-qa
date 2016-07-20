# -*- coding: utf-8 -*-
import requests


def test_post_should_work_properly():
    ads_data = {
        "propertyCode": "763088",
        "propertyType": "Apartamento",
        "description": "Apartamento Novo - Bairro Botafogo ",
        "updatedAt": "2016-05-23"
    }
    post_api_response = requests.post(
        'http://httpbin.org/post',
        data=ads_data
    )

    assert post_api_response.status_code == 200
    assert 'form' in post_api_response.json()
    post_api_data = post_api_response.json()['form']
    assert post_api_data['propertyCode'] == ads_data['propertyCode']
    assert post_api_data['propertyType'] == ads_data['propertyType']
    assert post_api_data['description'] == ads_data['description']
    assert post_api_data['updatedAt'] == ads_data['updatedAt']
