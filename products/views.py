from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.


def list_products(request):
    products = Product.objects.all()
    return render(request, 'list_products.html', {'products': products})


def get_product_form(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    return render(request, 'partials/htmx_components/edit_product_form.html', {'form': form, 'product': product})


@require_http_methods(['POST'])
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST, instance=product)  
    if form.is_valid():
        form.save()
        products = Product.objects.all()
        return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})
    return render(request, 'partials/htmx_components/edit_product_form.html', {'form': form, 'product': product})
