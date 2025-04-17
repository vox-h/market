from django.shortcuts import render

from goods.models import Products


# Create your views here.
def catalog(request):
    goods = Products.objects.all()

    context = {
        'title': 'Home - Главная',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug, product_id):
    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'goods/product.html', context=context)
