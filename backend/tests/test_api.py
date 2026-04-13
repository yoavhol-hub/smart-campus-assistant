from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "running" in response.json()["message"].lower()


@patch("app.main.generate_ai_answer")
def test_ask_valid_question(mock_generate_ai_answer):
    mock_generate_ai_answer.return_value = "The computer lab is in Building B."

    response = client.post("/ask", json={"question": "Where is the computer lab?"})

    assert response.status_code == 200

    data = response.json()
    assert "question" in data
    assert "category" in data
    assert "answer" in data
    assert "used_fallback" in data
    assert data["question"] == "Where is the computer lab?"
    assert data["answer"] == "The computer lab is in Building B."


def test_ask_empty_question():
    response = client.post("/ask", json={"question": ""})
    assert response.status_code == 422


def test_ask_whitespace_question():
    response = client.post("/ask", json={"question": "   "})
    assert response.status_code == 422


def test_ask_too_short_question():
    response = client.post("/ask", json={"question": "hi"})
    assert response.status_code == 422