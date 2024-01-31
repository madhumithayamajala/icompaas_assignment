from flask import Flask, request, jsonify

from app import app


@app.route('/')
def index():
    return 'Hello, iCompaas Assignment!'


@app.route('/v1/sanitized/input/', methods=['POST'])
def check_sanitization():
    try:
        payload = request.get_json()

        if 'input' not in payload:
            return jsonify({'error': 'Missing input field in the JSON payload'}), 400

        input_string = payload['input']

        sql_injection_characters = [";", "--", "DROP", "DELETE", "UPDATE", "INSERT"]
        if not any(char.lower() in input_string.lower() for char in sql_injection_characters):
            result = {'result': 'sanitized'}
        else:
            result = {'result': 'unsanitized'}

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
