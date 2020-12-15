import requests
import pytest
from app import app


@pytest.fixture
def get_request():
    # r = requests.get(url='http://0.0.0.0:5000')
    r =  app.test_client()
    return r

def test_status_code(get_request):
    """
    r = get_request
    status = r.status_code
    """
    r = get_request.get('/')
    status = int(r.status.split()[0])
    assert status == 200, 'Status is 200.'

def test_message(get_request):
    """
    r = get_request
    text = r.text
    """
    text = get_request.get('/').get_data(as_text=True)
    assert text == 'Data Engineer Schulung: Herzlich Willkommen Teilnehmer!'
