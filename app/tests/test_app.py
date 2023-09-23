"""
test_app.py: It contents flask app tests.
"""

__author__      = "alvertogit"
__copyright__   = "Copyright 2018-2023"


import pytest
import json
import sys

def test_index(client):
    response = client.get("/")
    # check response
    assert response.status_code == 200
    assert response.data == b"Deep Learning on Flask"

def test_api(client):
    # server REST API endpoint url and example image path
    SERVER_URL = "http://127.0.0.1:5000/api/predictlabel"
    IMAGE_PATH = "../app/static/4.jpg"

    # create payload with image for request
    image = open(IMAGE_PATH, "rb")
    payload = {"file": image}
    response = client.post(SERVER_URL, data=payload)

    # check response
    assert response.status_code == 200

    # JSON for