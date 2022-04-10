from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProductInLineSerialzier(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product_detail',lookup_field='pk',read_only=True)
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    this_is_not_real = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)