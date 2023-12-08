from django.shortcuts import render
from django.urls import reverse_lazy, reverse
# from .models import Product

# Create your views here.


def home(request):
    return render(request, 'home.html', {})
    # products = Product.objects.all()

    # return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, template_name='about.html',)


def privacy(request):
    return render(request, template_name='privacy.html',)

