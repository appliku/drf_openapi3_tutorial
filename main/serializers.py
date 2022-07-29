from rest_framework import serializers
from main import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name', 'slug',)


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductFeature
        fields = ('product', 'feature', 'ordering',)


class ProductSerializer(serializers.ModelSerializer):
    features = ProductFeatureSerializer(many=True)

    class Meta:
        model = models.Product
        fields = ('name', 'slug', 'category', 'description', 'price', 'features',)


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Feature
        fields = ('name', 'description',)


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ('image', 'is_main', 'product',)
