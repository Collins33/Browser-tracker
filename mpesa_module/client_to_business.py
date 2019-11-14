import os

import requests
from generate_credentials import generate_credentials

# REGISTER THE URLs FIRST

access_token = generate_credentials()
short_code = os.getenv('SHORT_CODE')
msisdn_number = os.getenv('MSISDN')


def register_urls():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": short_code,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://muru35portfolio.herokuapp.com",
               "ValidationURL": "https://muru35portfolio.herokuapp.com"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


def simulate_client_to_business_transaction():
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {"ShortCode": short_code,
               "CommandID": "CustomerPayBillOnline",
               "Amount": "2",
               "Msisdn": msisdn_number,
               "BillRefNumber": "12345678"}

    response = requests.post(api_url, json=request, headers=headers)

    print(response.text)


simulate_client_to_business_transaction()
