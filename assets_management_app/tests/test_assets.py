import pytest
from fastapi.testclient import TestClient

from app.main import app
import app.store as store_module


@pytest.fixture(autouse=True)
def clear_store():
    store_module.assets.clear()
    yield
    store_module.assets.clear()


client = TestClient(app)


def test_list_assets_empty():
    response = client.get("/assets")
    assert response.status_code == 200
    assert response.json() == []


def test_add_asset_returns_201():
    payload = {"name": "ThinkPad X1", "asset_type": "hardware", "description": "Laptop"}
    response = client.post("/assets", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "ThinkPad X1"
    assert data["asset_type"] == "hardware"
    assert data["description"] == "Laptop"
    assert "id" in data
    assert "created_at" in data
    assert "updated_at" in data
    assert data["os_info"] is None


def test_add_asset_with_os_info():
    payload = {
        "name": "ThinkPad X1",
        "asset_type": "hardware",
        "os_info": {"name": "Linux", "version": "Ubuntu 24.04"},
    }
    response = client.post("/assets", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["os_info"]["name"] == "Linux"
    assert data["os_info"]["version"] == "Ubuntu 24.04"


def test_list_assets_after_add():
    payload = {"name": "VS Code", "asset_type": "software"}
    client.post("/assets", json=payload)
    response = client.get("/assets")
    assert response.status_code == 200
    assets = response.json()
    assert len(assets) == 1
    assert assets[0]["name"] == "VS Code"


def test_add_asset_missing_required_field():
    response = client.post("/assets", json={"asset_type": "hardware"})
    assert response.status_code == 422
