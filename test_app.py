import requests
import pytest


@pytest.fixture
def get_request():
    r = requests.get(url='http://0.0.0.0:5000')
    return r

def test_status_code(get_request):
    r = get_request
    assert r.status_code == 200, 'Status is 200.'

def test_message(get_request):
    r = get_request
    assert r.text == 'Data Engineer Schulung: Herzlich Willkommen Teilnehmer!'
