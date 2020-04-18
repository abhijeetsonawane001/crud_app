import pytest


def test_home_page_render(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Flask Boilerplate" in response.data
