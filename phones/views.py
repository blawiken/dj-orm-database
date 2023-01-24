from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')

    def sort_phones(param):    
        phones = Phone.objects.all().order_by(param)
        context = {'phones': phones}
        return render(request, template, context)

    if sort == 'name':
        return sort_phones('name')
    elif sort == 'min_price':
        return sort_phones('price')
    elif sort == 'max_price':
        return sort_phones('-price')
    else:
        return sort_phones('id')


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
