from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Product
from .forms import ProductForm


def check_product(request):
    product = request.GET.get('product')
    products = Product.objects.filter(name=product)
    return render(request, 'partials/htmx_components/check_product.html', {'products': products})


def save_product(request):
    name = request.POST.get('product')
    price = request.POST.get('price')

    product = Product(
        name=name,
        price=price
    )

    product.save()
    products = Product.objects.all()
    return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    # Busca todos os produtos existentes no banco de dados pelo respectivo ID
    products = Product.objects.all()
    return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})


def get_product_form(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)
    return render(request, 'partials/htmx_components/edit_product_form.html', {'form': form, 'product': product})

@csrf_exempt
@require_http_methods(['POST'])
def edit_product(request, id):
    # Obter o produto existente pelo ID
    product = get_object_or_404(Product, id=id)

    # Obter os novos dados do produto do corpo da requisição
    product_name = request.POST.get('product')  # Nome do campo do formulário deve ser 'name'
    price = request.POST.get('price')

    # Verificar se os campos obrigatórios não estão vazios
    if not product_name or price is None:
        # Trate o erro de campos vazios aqui, talvez redirecionando ou retornando uma mensagem de erro
        return render(request, 'partials/htmx_components/list_all_products.html', {'error': 'Name and price cannot be empty', 'products': Product.objects.all()})

    # Atualizar os campos do produto existente
    product.name = product_name
    product.price = price

    # Salvar o produto editado
    product.save()

    # Buscar todos os produtos novamente após a edição
    products = Product.objects.all()

    # Retornar a lista atualizada de produtos
    return render(request, 'partials/htmx_components/list_all_products.html', {'products': products})