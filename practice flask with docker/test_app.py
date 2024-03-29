from app import app
import pytest
@pytest.fixture
def client():
    app.config['TESTING']= True
    client = app.test_client()
    yield client

def test_home(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b'hello, this is our first flask website'