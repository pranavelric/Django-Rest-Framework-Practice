from tkinter import N
from django.conf import settings
from django.db import models
from django.db.models import Q
import random


User = settings.AUTH_USER_MODEL

TAGS_MODEL_VALUES = ["electronics","cars","boats","movies","cameras"]


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)
    def search(self,query,user=None):
        lookup=  Q(title__icontains=query)| Q(content__icontains=query)
        qs= self.is_public().filter(lookup)
        if user is not None:
            qs2 = qs.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self,*args,**kwargs):
        return ProductQuerySet(self.model,using=self._db)
    def  search(self,query,user=None):
        return self.get_queryset().is_public().filter(title__icontains=query)

class Product(models.Model):
    
    user = models.ForeignKey(User, default=1,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)
    public = models.BooleanField(default=True)
    objects = ProductManager()

    def get_absolute_url(self):
        return f"/api/products/{self.pk}/"
    
    @property
    def endpoint(self):
        return self.get_absolute_url()

    @property
    def path(self):
        return f"/products/{self.pk}"

    @property
    def body(self):
        return self.content

    def is_public(self):
        return self.public

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]


    @property
    def sale_price(self):
        return "%0.2f" % (float(self.price)*0.8)