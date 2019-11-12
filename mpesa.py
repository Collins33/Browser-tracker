import os
from datetime import datetime
from requests.auth import HTTPBasicAuth
import base64

import requests

phone_number = os.getenv('PHONE_NUMBER')
business_short_code = os.getenv('BUSINESS_SHORT_CODE')
pass_key = os.getenv('PASS_KEY')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

unformated_time = datetime.now()
formatted_date = unformated_time.strftime("%Y%m%d%H%M%S")

business_short_code+pass_key+formatted_date
date_to_encode = business_short_code+pass_key+formatted_date
encoded_string = base64.b64encode(
    date_to_encode.encode())  # encode it into binary
decoded_password = encoded_string.decode('utf-8')


def generate_credentials():
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    auth_response = requests.get(
        api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return auth_response.json()['access_token']


def lipa_na_mpesa():
    access_token = generate_credentials()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": business_short_code,
        "Password": decoded_password,
        "Timestamp": formatted_date,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": phone_number,
        "PartyB": business_short_code,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://muru35portfolio.herokuapp.com",
        "AccountReference": "11223456",
        "TransactionDesc": "Pay school fees"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


lipa_na_mpesa()
