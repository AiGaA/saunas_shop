from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, StoveFeature, WindowFeature

# Create your views here.


def all_products(request):
    """ A view to return the all products, including sorting and search queries page """ 

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to return the the specific product to see description and a total price """ 

    product = get_object_or_404(Product, pk=product_id)
    stove_feature = StoveFeature.objects.all()
    window_feature = WindowFeature.objects.all()

    context = {
        'product': product,
        'stove_feature': stove_feature,
        'window_feature': window_feature,
    }

    return render(request, 'products/product_detail.html', context)