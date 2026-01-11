import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import pytest
from app import app as flask_app


@pytest.fixture()
def client():
    flask_app.config.update(TESTING=True)
    return flask_app.test_client()


def test_index_ok(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"


def test_health_ok(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "healthy"


def test_add_ok(client):
    resp = client.get("/add?x=2&y=3")
    assert resp.status_code == 200
    assert resp.get_json()["result"] == 5.0


def test_add_missing_param(client):
    resp = client.get("/add?x=2")
    assert resp.status_code == 400
