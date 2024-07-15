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
    customer = request.user.customer
    try:
        # Intentar obtener la orden del cliente que no esté completada
        order = Order.objects.get(customer=customer, completed=False)
    except Order.DoesNotExist:
        # Si no existe dicha orden, creamos una nueva
        order = Order.objects.create(customer=customer, completed=False)
    
    items = OrderItem.objects.filter(order=order)
    items_data = []
    for item in items:
        product = item.product
        items_data.append({
            'name': product.name,
            'price': product.price,
            'image_url': product.imageURL,
            'quantity': item.quentity,
        })
    
    
    context = {
        'order': order,
        'items': items_data,
    }
    
    return render(request, 'ecommerceApp/cart.html', context)