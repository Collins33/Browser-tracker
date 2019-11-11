import requests
import os

phone_number = os.getenv('PHONE_NUMBER')
business_short_code = os.getenv('BUSINESS_SHORT_CODE')
pass_key = os.getenv('PASS_KEY')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

# access_token = "Access-Token"
# api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
# headers = { "Authorization": "Bearer %s" % access_token }
# request = {
#     "BusinessShortCode": " ",
#     "Password": " ",
#     "Timestamp": " ",
#     "TransactionType": "CustomerPayBillOnline",
#     "Amount": "5",
#     "PartyA": " ",
#     "PartyB": " ",
#     "PhoneNumber": " ",
#     "CallBackURL": "https://muru35portfolio.herokuapp.com",
#     "AccountReference": "11223456",
#     "TransactionDesc": "Pay school fees"
# }
  
# response = requests.post(api_url, json = request, headers=headers)
  
# print (response.text)