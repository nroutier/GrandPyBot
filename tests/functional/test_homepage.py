import pytest
from app import create_app
from config import Config

class TestConfig(Config):
    TESTING = True


@pytest.fixture
def test_client():
    flask_app = create_app(TestConfig)
 
    testing_client = flask_app.test_client()

    yield testing_client
 
def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert 'GrandPy Bot' in response.get_data().decode('utf-8')
    assert 'Un papi qui en sait long en géographie !' in response.get_data().decode('utf-8')

def  test_query_route(test_client):
    """
    GIVEN a Flask application
    WHEN the '/query/' page is requested (POST)
    THEN check the response is valid
    """
    mock_request_data = {"query": "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"}

    response = test_client.post('/query/', data = mock_request_data)
    assert response.status_code == 200

