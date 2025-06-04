from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    """Страница со всеми товарами с возможностью сортировки по
    возрастанию цены, убыванию цены и по алфавиту"""

    template = 'catalog.html'

    sort_by = request.GET.get('sort', 'name')

    if sort_by == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_by == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')

    context = {
        'phones': phones
    }
    return render(request, template, context)

def show_product(request, slug):
    """Страница продукта"""

    template = 'product.html'

    product = get_object_or_404(Phone, slug=slug)

    print(f'Product: {product.name}, Price: {product.price}, Release Date: {product.release_date}')

    context = {
        'product': product
    }
    return render(request, template, context)















