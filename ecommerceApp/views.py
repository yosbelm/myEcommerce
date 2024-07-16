from django.shortcuts import render, redirect
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
        order = Order.objects.get(customer=customer, completed=False)
    except Order.DoesNotExist:
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
            'idd': item.id
        })
    
    total = 0
    for i in items_data:
        cantidad = i['quantity']
        tot = int(i['price'])
        total += cantidad*tot
    
      
    compras_list =[] 
    for elemento in items_data:
        nombre = elemento['name']
        precio = elemento['price']
        cantidad = elemento['quantity']
        tot = int(precio) * int(cantidad)
        compras_list.append({
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad,
            'tot': tot
        })    
    print('----------------------------------')
    print(compras_list)
    print('----------------------------------')
    context = {
        'order': order,
        'items': items_data,
        'total': total,
        'compras_list': compras_list,
    }
    return render(request, 'ecommerceApp/cart.html', context)

def delete_item(request, id):
    item = OrderItem.objects.get(id=id)
    print('****************************')
    print(item.id)
    item.delete()
    return redirect('cart') 
    
    