from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json


# Create your views here.
def productItem(request):
    productos = Product.objects.all()
    user_name = request.user
    usuario = request.user.id
    
    order = Order.objects.get(customer=usuario)
    prod = OrderItem.objects.filter(order=order)
    items_data = []
    cantidad_items = 0
    for item in prod:
        items_data.append({
            'quantity': item.quentity,
        })
        
    for i in items_data:
        cantidad = i['quantity']
        cantidad_items += cantidad
    
    print(usuario)
    print(order)
    print(prod)
    print(items_data)
    print(cantidad_items)
    context = {'productos': productos,
               'user_name': user_name,
               'cantidad_items': cantidad_items,
               }
    return render(request, 'ecommerceApp/ecomm.html', context)


def cantid(request):
    cantidad = OrderItem.objects.all()
    print(cantidad)
    print('0000000000000000000000000000000000000000000000000000000000')
    context = {}
    return render(request, 'ecommerceApp/base.html', context)


def signin(request):
    return render(request, 'ecommerceApp/signin.html')

def create_user(request):
    return render(request, 'ecommerceApp/signup.html')

def cart(request):
    usuario = request.user.id
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
            'idd': item.id,
            'id': product.id
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
    cantidad_items = 0
    for i in compras_list:
        cantidad = i['cantidad']
        cantidad_items += cantidad
        
      
    print('----------------------------------')
    print(items_data)
    print('----------------------------------')
    print(items)
    
    context = {
        'order': order,
        'items': items_data,
        'total': total,
        'compras_list': compras_list,
        'cantidad_items' : cantidad_items,
        'usuario': usuario,
    }
    return render(request, 'ecommerceApp/cart.html', context)

def delete_item(request, id):
    item = OrderItem.objects.get(id=id)
    print('****************************')
    print(item.id)
    item.delete()
    return redirect('cart') 

def updateItem(request):
    try:
        data = json.loads(request.body)
        productId = data['productId']
        action = data['action']
        print(productId)
        print(action)
        
        customer = request.user.customer
        product = Product.objects.get(id=productId)
        order, created = Order.objects.get_or_create(customer = customer)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        
        if action == 'add':
            orderItem.quentity = (orderItem.quentity + 1)
        elif action == 'remove':
            orderItem.quentity = (orderItem.quentity - 1)
            
        orderItem.save()
        
        if orderItem.quentity <= 0:
            orderItem.delete()
        
        
        return JsonResponse('Hiiiii', safe=False)
    except:
        return JsonResponse('Hi there', safe=False)
    
    