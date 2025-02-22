from django.shortcuts import render, get_object_or_404
from .models import Phone


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by('name')

    return render(request, 'catalog.html', {'phones': phones})



def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'catalog.html', {'phones': phones})

