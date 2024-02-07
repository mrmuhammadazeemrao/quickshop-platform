from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_products_without_parameters():
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 1


def test_get_products_with_query():
    response = client.get("/products?query=test")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_products_with_category():
    response = client.get("/products?category=example_category")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_products_with_query_and_category():
    response = client.get("/products?query=test&category=example_category")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
