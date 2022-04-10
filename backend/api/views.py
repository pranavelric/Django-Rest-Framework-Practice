import json
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):


    ser = ProductSerializer(data =request.data)
    if ser.is_valid(raise_exception=True):
        print(ser.data)
        return Response(ser.data)
    return Response({"invalid": "not good data"}, status=400)
 
