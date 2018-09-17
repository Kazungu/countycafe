import requests
from requests.auth import HTTPBasicAuth

consumer_key = "GbGKA2zZ6Zd5MsJazG1XPNOym6bDuEuV "
consumer_secret = "U3MIAc4GygmAXGYK"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print (r)
