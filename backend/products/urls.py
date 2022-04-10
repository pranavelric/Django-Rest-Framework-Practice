from django.contrib import admin
from django.urls import path, include
from .views import ProductDetailAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductListCreateAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view(),name='product_detail'),
    path('',ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', ProductDestroyAPIView.as_view()),

]
