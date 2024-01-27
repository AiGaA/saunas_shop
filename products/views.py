from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, ProductFeature, ProductWithFeature

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
    features = ProductFeature.objects.all()

    if request.method == 'POST':
        selected_features = request.POST.getlist('features')
        total_price = product.price + sum(ProductFeature.objects.filter(pk__in=selected_features).values_list('price', flat=True))
    else:
        total_price = product.price

    context = {
        'product': product,
        'features': features,
        'total_price': total_price,
    }

    return render(request, 'products/product_detail.html', context)
