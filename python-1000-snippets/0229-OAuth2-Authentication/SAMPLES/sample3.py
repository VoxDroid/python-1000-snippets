# sample3.py
# Demonstrate token refresh in a simple OAuth2 server/client.

from flask import Flask, request, jsonify
import threading
import time
import requests


CLIENT_ID = 'demo-client'
CLIENT_SECRET = 'demo-secret'
ACCESS_TOKEN = 'demo-access-token-v1'
REFRESH_TOKEN = 'demo-refresh-token'


def create_app():
    app = Flask(__name__)

    @app.route('/token', methods=['POST'])
    def token():
        grant_type = request.form.get('grant_type')

        if grant_type == 'client_credentials':
            client_id = request.form.get('client_id')
            client_secret = request.form.get('client_secret')
            if client_id != CLIENT_ID or client_secret != CLIENT_SECRET:
                return jsonify(error='invalid_client'), 401

            return jsonify(
                access_token=ACCESS_TOKEN,
                token_type='bearer',
                expires_in=1,  # expire quickly to demonstrate refresh
                refresh_token=REFRESH_TOKEN,
            )

        if grant_type == 'refresh_token':
            refresh_token = request.form.get('refresh_token')
            if refresh_token != REFRESH_TOKEN:
                return jsonify(error='invalid_grant'), 400
            return jsonify(access_token='demo-access-token-v2', token_type='bearer', expires_in=3600)

        return jsonify(error='unsupported_grant_type'), 400

    @app.route('/resource')
    def resource():
        auth = request.headers.get('Authorization', '')
        if auth not in (f'Bearer {ACCESS_TOKEN}', 'Bearer demo-access-token-v2'):
            return jsonify({'error': 'invalid_token'}), 401
        return jsonify({'message': 'Protected resource accessed.'})

    return app


def run_server():
    app = create_app()
    server = threading.Thread(target=lambda: app.run(host='127.0.0.1', port=5001, debug=False, use_reloader=False))
    server.daemon = True
    server.start()
    time.sleep(0.2)
    return server


def main():
    server = run_server()

    # Initial token request (client credentials)
    token_resp = requests.post(
        'http://127.0.0.1:5001/token',
        data={
            'grant_type': 'client_credentials',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    token = token_resp.json()
    print('Initial token:', token)

    # Wait for token expiry, then try resource access
    time.sleep(1.1)
    resp = requests.get('http://127.0.0.1:5001/resource', headers={'Authorization': f"Bearer {token['access_token']}"})
    print('Resource call with expired token:', resp.status_code, resp.json())

    # Refresh token
    refresh_resp = requests.post(
        'http://127.0.0.1:5001/token',
        data={'grant_type': 'refresh_token', 'refresh_token': token['refresh_token']},
    )
    new_token = refresh_resp.json()
    print('Refreshed token:', new_token)

    # Use refreshed token
    resp2 = requests.get('http://127.0.0.1:5001/resource', headers={'Authorization': f"Bearer {new_token['access_token']}"})
    print('Resource call with refreshed token:', resp2.status_code, resp2.json())


if __name__ == '__main__':
    main()
