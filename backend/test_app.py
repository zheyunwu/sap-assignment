import pytest
from app import app
from io import BytesIO

@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """ Test the home route. """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_get_images(client):
    """ Test the GET /images route. """
    response = client.get('/images')
    assert response.status_code == 200
    assert 'items' in response.json
    assert 'total' in response.json

def test_post_images_valid(client):
    """ Test the POST /images route with valid data. """
    data = {
        'tag_name': 'unit_test_image',
        'dockerfile': (BytesIO(b'FROM busybox'), 'unit_test_image.Dockerfile') # simulate a dockerfile
    }
    response = client.post('/images', data=data, content_type='multipart/form-data')
    assert response.status_code == 202

def test_post_images_invalid(client):
    """ Test the POST /images route with invalid data. """
    response = client.post('/images', data={})
    assert response.status_code == 400