from ninja import NinjaAPI
from app.json_web_token import JsonWebToken
from ninja.security import HttpBearer
from django.views.decorators.csrf import csrf_exempt

from app.user_info import get_user_info, get_user_id


def validate_token(token: str):
    return JsonWebToken(token).validate()


def validate_permission(permissions: list[str], required_permissions: list[str]):
    required_permissions_set = set(required_permissions)
    user_permissions_set = set(permissions.get("permissions"))
    satisfies_required = required_permissions_set.issubset(user_permissions_set)
    return satisfies_required


def authorization(token, required_permissions):
    token_validation = validate_token(token.strip())
    if token_validation == 'BadCredentialsException':
        return False
        # return {"message": "BadCredentialsException"}
    if token_validation == 'UnableCredentialsException':
        return False
        # return {"message": "UnableCredentialsException"}

    permission_validation = validate_permission(token_validation, required_permissions)
    if permission_validation:
        return True
    else:
        return False


# AUTHORIZATION
class NormalUser(HttpBearer):
    def authenticate(self, request, token):
        required_permissions = []
        x = request.headers.get("Authorization").split(" ")
        is_authorized = authorization(x[1], required_permissions)
        if is_authorized:
            return True
        else:
            return False


class Admin(HttpBearer):
    def authenticate(self, request, token):
        required_permissions = ["user:admin"]
        x = request.headers.get("Authorization").split(" ")
        is_authorized = authorization(x[1], required_permissions)
        if is_authorized:
            return True
        else:
            return False


api = NinjaAPI(auth=[NormalUser(), Admin()], csrf=True, title="Auth0 Sample")


@api.get('/admin', auth=Admin())
@csrf_exempt
def admin(request):
    user_id = get_user_id(request.headers)
    user_info = get_user_info(user_id)
    return {"message": "ADMIN", "user_email": user_info.get("email")}


@api.get('/protected', auth=NormalUser())
@csrf_exempt
def protected(request):
    return {"message": "ADMIN and NORMAL USER"}


@api.get("/hello", auth=NormalUser())
@csrf_exempt
def hello(request):
    return {"message": "ADMIN and NORMAL USER"}


@api.get("/public", auth=None)
@csrf_exempt
def public(request):
    return {"message": "PUBLIC"}