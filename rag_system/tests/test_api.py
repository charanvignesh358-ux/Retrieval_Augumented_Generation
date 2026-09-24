from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Enterprise RAG System API"}

def test_ingest_endpoint_exists():
    # We expect 422 because we didn't send a file, but it proves the endpoint exists
    response = client.post("/api/v1/ingest")
    assert response.status_code == 422

def test_query_endpoint_exists():
    # We expect 422 because we didn't send a body
    response = client.post("/api/v1/query", json={})
    assert response.status_code == 422
