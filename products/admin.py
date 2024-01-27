from django.contrib import admin
from .models import Product, Category, ProductFeature, ProductWithFeature

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'stove_feature',
        'window_feature',
        'price',
        'description',
    )

    ordering= ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'stove_type',
        'name',
    )

class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'product_type',
        'price',
    )

class ProductWithFeatureAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'features',
    )
    
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductFeature)
admin.site.register(ProductWithFeature)