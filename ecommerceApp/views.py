from django.shortcuts import render, redirect
from .models import *
from django.http import JsonResponse
import json
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse


# Create your views here.
def productItem(request):
    productos = Product.objects.all()
    user_name = request.user
    
    usuario = request.user.customer
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
    if request.method == 'GET':
        print('utliza metodo get')
    else:
        user = authenticate(request, username=request.POST['name'], password=request.POST['password'])
        if user is None:
            return render(request, 'ecommerceApp/signin.html', {'error': 'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('home')

    return render(request, 'ecommerceApp/signin.html')
        


def create_user(request):
    if request.method == 'GET':
        print('metodo get')
        return render(request, 'ecommerceApp/signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(request.POST)
                user = User.objects.create_user(username=request.POST['name'], password=request.POST['password1'])
                print(user)
                user.save()
                login(request, user)
                return redirect('home')
            except:
                error_user = 'User already exists'
                return render(request, 'ecommerceApp/signup.html', {'error_user':error_user})
        else:
            error = 'The passwords do not match'
            return render(request, 'ecommerceApp/signup.html', {'error':error})
        


def signout(request):
    logout(request)
    return redirect('signin')


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
        tot = float(i['price'])
        total += cantidad*tot
    
    compras_list =[] 
    for elemento in items_data:
        nombre = elemento['name']
        precio = elemento['price']
        cantidad = elemento['quantity']
        tot = float(precio) * float(cantidad)
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
    return redirect('carr') 



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
    


def checkout(request):
    # code to show the total of items in the cart
    usuario = request.user.customer
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
    # code to show the total of items in the cart
    
    context= {
        'cantidad_items': cantidad_items
    }
    return render(request, 'ecommerceApp/checkout.html', context)



def details(request, id):
    producto = Product.objects.get(id=id)
    image = producto.imageURL
    precio = producto.price
    name = producto.name
    description = producto.description
    print('-------------------------')
    print(image)
    
    # code to show the total of items in the cart
    usuario = request.user.customer
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
    # code to show the total of items in the cart
    
    context={'producto':producto, 
             'precio': precio,
             'name': name,
             'image': image,
             'description':description,
             'cantidad_items': cantidad_items,
             }
    return render(request, 'ecommerceApp/details.html', context) 



def home(request):
    productos = Product.objects.all()
    
    # code to show the total of items in the cart
    usuario = request.user.customer
    print(usuario)
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
    # code to show the total of items in the cart
    
    cheap_productos=[]
    for product in productos:
        if product.price < 100:
            cheap_productos.append(product)
    print('iiiiiiiiiiiiiiiiiiiiiiiiiiiii')  
    print(cheap_productos)  
    context={
        'usuario': usuario,
        'cantidad_items': cantidad_items,
        'productos':productos,
        'cheap_productos': cheap_productos,
    }
    return render(request, 'ecommerceApp/home.html', context) 