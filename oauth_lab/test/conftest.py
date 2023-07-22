import pytest
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from run import APP

@pytest.fixture
def app():
    yield APP

@pytest.fixture
def client(app):
    return app.test_client()