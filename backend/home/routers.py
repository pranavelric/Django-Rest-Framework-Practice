from rest_framework.routers import DefaultRouter


from products.viewsets import ProductGenericViewSet, ProductViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
urlpatterns = router.urls