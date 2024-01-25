from django.contrib import admin
from .models import Product, Category, StoveFeature, WindowFeature

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

class StoveFeatureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'stove_type',
        'price',
    )

class WindowFeatureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'window_type',
        'price',
    )
    
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(StoveFeature)
admin.site.register(WindowFeature)