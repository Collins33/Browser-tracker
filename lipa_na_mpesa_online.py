import os
from requests.auth import HTTPBasicAuth
import requests

from generate_credentials import generate_credentials
from utils import format_date, encode_password_String

phone_number = os.getenv('PHONE_NUMBER')
business_short_code = os.getenv('BUSINESS_SHORT_CODE')
pass_key = os.getenv('PASS_KEY')

formatted_date = format_date()
decoded_password = encode_password_String(
    business_short_code, pass_key, formatted_date)


def lipa_na_mpesa_online():
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


lipa_na_mpesa_online()
