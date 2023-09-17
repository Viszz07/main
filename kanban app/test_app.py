import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('/')
    assert b'Kanban Board' in response.data

def test_add_task(client):
    response = client.post('/add_task', data= 'New Task')
    assert b'New Task' not in response.data
    assert b'To Do' not in response.data

def test_move_task(client):
    client.post('/add_task', data={'task_name': 'Task to move', 'status': 'todo'})
    response = client.post('/move_task', data={'task_name': 'Task to move', 'current_status': 'todo', 'new_status': 'in_progress'})
    assert b'Task to move' not in response.data
    assert b'In Progress' not in response.data


def test_invalid_add(client):
    response = client.post('/add_task', data={'task_name': '', 'status': 'todo'})
    assert b'todo' not in response.data

if __name__ == '__main__':
    pytest.main()