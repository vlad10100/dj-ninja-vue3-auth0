import http.client
import json
from django.conf import settings
from auth0.management import Users

from app.json_web_token import JsonWebToken

# Auth0 Management API -> default
domain = settings.AUTH0_DOMAIN

# MACHINE Auth0 Test Client Machine
client_id = settings.AUTH0_CLIENT_ID
client_secret = settings.AUTH0_CLIENT_SECRET

# im not sure why the audience is like this...
# https://community.auth0.com/t/401-bad-audience/109494
audience = f"https://{domain}/api/v2/"
grant_type = "client_credentials"


def get_management_token():
    conn = http.client.HTTPSConnection(domain)
    payload = {"client_id": client_id,
               "client_secret": client_secret,
               "audience": audience,
               "grant_type": grant_type}

    headers = {'content-type': "application/json"}

    conn.request("POST", "/oauth/token", json.dumps(payload), headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    token = data.get("access_token")
    return token


def validate_token(token: str):
    return JsonWebToken(token).validate()


def get_user_id(headers):
    token = headers.get("Authorization").split(" ")[1]
    user_id = validate_token(token).get("sub")
    return user_id


def get_user_info(user_id):
    token = get_management_token()
    users = Users(domain=domain, token=token)
    user_info = users.get(id=user_id)

    return user_info
