from requests.auth import HTTPBasicAuth
import os
import requests

# security keys
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')


def generate_credentials():
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    auth_response = requests.get(
        api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return auth_response.json()['access_token']
