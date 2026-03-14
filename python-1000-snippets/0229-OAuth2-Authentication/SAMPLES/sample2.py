# sample2.py
# Demonstrate OAuth2 client credentials flow using requests-oauthlib.

import os

from flask import Flask, request, jsonify
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import threading
import time


CLIENT_ID = 'demo-client'
CLIENT_SECRET = 'demo-secret'
ACCESS_TOKEN = 'demo-access-token'


def create_app():
    app = Flask(__name__)

    @app.route('/token', methods=['POST'])
    def token():
        grant_type = request.form.get('grant_type')

        # Support client auth via form parameters or HTTP Basic auth
        auth = request.authorization
        if auth:
            client_id = auth.username
            client_secret = auth.password
        else:
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
        return jsonify({'message': 'Protected data accessed via OAuth2Session.'})

    return app


def run_server():
    app = create_app()
    server = threading.Thread(target=lambda: app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False))
    server.daemon = True
    server.start()
    time.sleep(0.2)
    return server


def main():
    # oauthlib blocks plain HTTP by default. For local test servers, allow insecure transport.
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    server = run_server()

    # Use requests-oauthlib’s BackendApplicationClient to perform client credentials flow.
    client = BackendApplicationClient(client_id=CLIENT_ID)
    oauth = OAuth2Session(client=client)

    token = oauth.fetch_token(
        token_url='http://127.0.0.1:5001/token',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
    )

    print('Fetched token:', token)
    resp = oauth.get('http://127.0.0.1:5001/resource')
    print('Resource response:', resp.json())


if __name__ == '__main__':
    main()
