from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "Test Description",
        "price": 9.99,
        "inventory_count": 100,
        "category": "Test Category"
    })
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
