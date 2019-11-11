import requests
import os
from datetime import datetime

phone_number = os.getenv('PHONE_NUMBER')
business_short_code = os.getenv('BUSINESS_SHORT_CODE')
pass_key = os.getenv('PASS_KEY')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

unformated_time =  datetime.now()
formatted_date = unformated_time.strftime("%Y%m%d%H%M%S")
print(formatted_date)

def lipa_na_mpesa():

  access_token = "Access-Token"
  api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
  headers = { "Authorization": "Bearer %s" % access_token }
  request = {
      "BusinessShortCode": business_short_code,
      "Password": " ",
      "Timestamp": formatted_date,
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "5",
      "PartyA": phone_number,
      "PartyB": " ",
      "PhoneNumber": phone_number,
      "CallBackURL": "https://muru35portfolio.herokuapp.com",
      "AccountReference": "11223456",
      "TransactionDesc": "Pay school fees"
  }
    
  response = requests.post(api_url, json = request, headers=headers)
    
  print (response.text)