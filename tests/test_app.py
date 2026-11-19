from app import app

client = app.test_client()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 2