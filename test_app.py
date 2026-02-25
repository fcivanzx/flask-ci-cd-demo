from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.data.decode("utf-8") == "¡Hola, CI/CD con DevOps!"