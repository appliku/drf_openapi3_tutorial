from rest_framework.routers import DefaultRouter

from main import api

router = DefaultRouter()
router.register(r'products', api.ProductViewSet, basename='products')
router.register(r'categories', api.CategoryViewSet, basename='categories')
router.register(r'features', api.FeatureViewSet, basename='features')
router.register(r'product_images', api.ProductImageViewSet, basename='product_images')

urlpatterns = router.urls
