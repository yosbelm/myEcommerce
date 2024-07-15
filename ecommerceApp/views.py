from django.shortcuts import render
from .models import *

# Create your views here.
def productItem(request):
    productos = Product.objects.all()
    
    context = {'productos': productos}
    return render(request, 'ecommerceApp/ecomm.html', context)


def signin(request):
    return render(request, 'ecommerceApp/signin.html')

def create_user(request):
    return render(request, 'ecommerceApp/signup.html')

def cart(request):
    return render(request, 'ecommerceApp/cart.html')