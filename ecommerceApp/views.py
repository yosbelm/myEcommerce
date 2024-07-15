from django.shortcuts import render
from .models import *

# Create your views here.
def productItem(request):
    user =  request.user
    productos = Product.objects.all()
    for i in productos:
        id = i.id
        imagens = Product.objects.get(id=id)
        image = imagens.image.url
        print(id)
    print(productos)
    print(imagens)
    print(image)
    context = {'productos': productos, 'image': image}
    return render(request, 'ecommerceApp/ecomm.html', context)


def signin(request):
    return render(request, 'ecommerceApp/signin.html')

def create_user(request):
    return render(request, 'ecommerceApp/create_user.html')

def cart(request):
    return render(request, 'ecommerceApp/cart.html')