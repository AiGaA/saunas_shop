from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name="products"),
    path('<product_id>', views.product_detail, name="product_detail"),

    # path('add_product/<product_id>/', views.add_product, name="add_product"),
]
