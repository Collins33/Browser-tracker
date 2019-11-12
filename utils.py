from datetime import datetime
import base64


def format_date():
    unformated_time = datetime.now()
    formatted_date = unformated_time.strftime("%Y%m%d%H%M%S")
    return formatted_date


def encode_password_String(business_short_code, pass_key, formatted_date):
    date_to_encode = business_short_code+pass_key+formatted_date
    encoded_string = base64.b64encode(
        date_to_encode.encode())  # encode it into binary
    decoded_password = encoded_string.decode('utf-8')
    return decoded_password
