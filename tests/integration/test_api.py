# -*- coding: utf-8 -*-
import requests

def test_post_should_work_properly():
    ads_data = {
        "propertyCode": "763088",
        "propertyType": "Apartamento",
        "description": "Bairro Botafogo - novo ícone de qualidade, Condomínio Clube com 2650 m². Varanda, 4 dormitórios sendo 1 suite, 2 vagas na escritura. Entrega: novembro/2016.",
        "updatedAt": "2016-05-23",
        "address": {
            "city": "Rio de Janeiro",
            "neighbourhood": "Botafogo",
            "number": 161,
            "complement": "Bl.02",
            "zipCode": "22271-100"
        },
        "photos": [
            {
                "url": "http://images2.brbrokers.com.br/CRM/763088/Medium42505.6554280903_d5cf61da1778e511843d02bfc0a80045160515033259fachada.jpg"
            },
        ]
    }
    post_api_response = requests.post(
        'http://httpbin.org/post',
        data=ads_data
    )

    assert post_api_response.status_code == 200
