import json
from app import app

def test_valid_input_should_be_sanitized():
    client = app.test_client()
    data = {'input': 'safe_input'}
    response = client.post('/v1/sanitized/input/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data) == {'result': 'sanitized'}


def test_invalid_input_should_be_unsanitized():
    client = app.test_client()
    data = {'input': 'unsafe_input;'}
    response = client.post('/v1/sanitized/input/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert json.loads(response.data) == {'result': 'unsanitized'}


def test_missing_input_field_should_return_error():
    client = app.test_client()
    data = {'invalid_key': 'some_value'}
    response = client.post('/v1/sanitized/input/', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 400
    assert json.loads(response.data) == {'error': 'Missing input field in the JSON payload'}
