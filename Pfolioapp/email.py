from django.conf import settings
import requests
import json
# Create your views here.




api_url = settings.API_URL
email = settings.EMAIL_HOST_USER


def is_valid_email(data):
    is_catchall_email = data.get('is_catchall_email', False)
    is_role_email = data.get('is_role_email', False)
    is_free_email = data.get('is_free_email', False)
    is_valid_format = data.get('is_valid_format', False)
    is_smtp_valid = data.get('is_smtp_valid', False)
    is_mx_found = data.get('is_mx_found', False),
    is_disposable_email = data.get('is_mx_found', False)
    if is_valid_format and is_mx_found and is_smtp_valid:
    #if is_valid_format and is_mx_found and is_smtp_valid and not is_catchall_email and not is_role_email and is_free_email:
        return True
    return False

def validate_email(email):
    response = requests.get(f"{api_url}&email={email}")
    response_data = response.json()
    print(response_data)
    if 'error' in response_data:
        raise ValueError(response_data['error']['message'])    
    return is_valid_email(response_data)
