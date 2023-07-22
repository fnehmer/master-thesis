def test_app_initialization(app, client):
    response = client.get('/api/')
    assert response.status_code == 200
    assert response.data == b"Hello World!"