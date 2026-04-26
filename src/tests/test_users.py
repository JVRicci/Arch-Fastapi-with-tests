from pytest import mark

def test_create_user(client):
    response = client.post('/users', json={
        'username': 'testuser',
        'email': '