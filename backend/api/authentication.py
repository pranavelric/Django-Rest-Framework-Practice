from ast import keyword
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.models import Token

class TokenAuth(TokenAuthentication):
    keyword = 'Bearer'