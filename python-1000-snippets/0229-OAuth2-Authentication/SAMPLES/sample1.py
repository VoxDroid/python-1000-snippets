# sample1.py
# Demonstrate a simple OAuth2 client credentials flow against a local token endpoint.

import threading
import time

import requests
from flask import Flask, request, jsonify


CLIENT_ID = 'demo-client'
CLIENT_SECRET = 'demo-secret'
ACCESS_TOKEN = 'demo-access-token'


def create_app():
    app = Flask(__name__)

    @app.route('/token', methods=['POST'])
    def token():
        grant_type = request.form.get('grant_type')
        client_id = request.form.get('client_id')
        client_secret = request.form.get('client_secret')

        if grant_type != 'client_credentials':
            return jsonify(error='unsupported_grant_type'), 400
        if client_id != CLIENT_ID or client_secret != CLIENT_SECRET:
            return jsonify(error='invalid_client'), 401

        return jsonify(access_token=ACCESS_TOKEN, token_type='bearer', expires_in=3600)

    @app.route('/resource')
    def resource():
        auth = request.headers.get('Authorization', '')
        if auth != f'Bearer {ACCESS_TOKEN}':
            return jsonify({'error': 'invalid_token'}), 401
        return jsonify({'message': 'This is protected data.'})

    return app


def run_server():
    app = create_app()
    server = threading.Thread(target=lambda: app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False))
    server.daemon = True
    server.start()
    # Give the server a moment to start
    time.sleep(0.2)
    return server


def main():
    server = run_server()

    try:
        token_resp = requests.post(
            'http://127.0.0.1:5001/token',
            data={
                'grant_type': 'client_credentials',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
        token_data = token_resp.json()
        print('Token response:', token_data)

        access_token = token_data.get('access_token')
        resp = requests.get(
            'http://127.0.0.1:5001/resource',
            headers={'Authorization': f'Bearer {access_token}'},
        )
        print('Resource response:', resp.json())
    finally:
        # Flask server thread will exit when main thread exits
        pass


if __name__ == '__main__':
    main()
