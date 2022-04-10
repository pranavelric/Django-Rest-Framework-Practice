from django.contrib import admin
from django.urls import path, include
from .views import SearchListView
urlpatterns = [
    path('',SearchListView.as_view(),name='search'),
   
]
