from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer
from django.db.models import Q 
from . import client
from rest_framework.response import Response

class SearchListView(generics.ListAPIView):
   
   def get(self,request,*args,**kwargs):
    user =None
    if request.user.is_authenticated:
        user= request.user.username
    public =str(request.GET.get('public'))!="False"
    query = request.GET.get('q')
    tags = request.GET.get('tag') or None
    print(request.GET)
    print(public)
    print(query)
    if not query:
        return Response('',status=400)
    results = client.perform_search(query,tags = tags,user=user,public=public)
    return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        q = self.request.GET.get('q')
        lookup=  Q(title__icontains=q)| Q(content__icontains=q)
        results = Product.objects.none()
        if q is not None:
            user = None 
            if self.request.user.is_authenticated:
                user=  self.request.user
            results = qs.filter(user=user).filter(lookup)
        return results