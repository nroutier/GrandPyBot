import pytest
from config import Config
from app import create_app

class TestConfig(Config):
    TESTING = True

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app

@pytest.fixture
def test_client(app):
    with app.test_client() as test_client:
        yield test_client