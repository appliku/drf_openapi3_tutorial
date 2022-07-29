from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated

from main import models
from main import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing categories.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing products.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class FeatureViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing features.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.FeatureSerializer
    queryset = models.Feature.objects.all()


class ProductImageViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing product images.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()
    parser_classes = (MultiPartParser, JSONParser)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product', ]
