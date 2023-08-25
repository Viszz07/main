import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_login_page(client):
    response = client.get('/')
    assert b'Login' in response.data
    assert response.status_code == 200

def test_successful_login(client):
    response = client.post('/', data={'email': 'test@example.com', 'password': 'password'}, follow_redirects=True)
    assert b'Logged in with email: test@example.com' in response.data

def test_missing_fields(client):
    response = client.post('/', data={'email': '', 'password': ''}, follow_redirects=True)
    assert b'Logged in with email: ' in response.data

if __name__ == '__main__':
    pytest.main()
