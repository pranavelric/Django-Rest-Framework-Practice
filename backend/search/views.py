from rest_framework import generics

from products.models import Product
from products.serializers import ProductSerializer
from django.db.models import Q 

class SearchListView(generics.ListAPIView):
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