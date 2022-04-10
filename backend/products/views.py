from cgitb import lookup
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from rest_framework import mixins
from api.mixins import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin)


class ProductListCreateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validate_data.get('title')
        content = serializer.validate_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user,content=content)




class ProductDetailAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductUpdateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field=  'pk'

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content= instance.title 

class ProductDestroyAPIView(UserQuerySetMixin,StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field=  'pk'

    