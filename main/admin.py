from django.contrib import admin
from main import models


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)


class ProductFeatureInline(admin.TabularInline):
    model = models.ProductFeature
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureInline, ]


admin.site.register(models.Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ProductImage, ProductImageAdmin)


class FeatureAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Feature, FeatureAdmin)
