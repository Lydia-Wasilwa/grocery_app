from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .cart import Cart

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        # Get quantity
        quantity = int(request.POST.get('quantity', 1))
        
        # Check if we should OVERRIDE the number (Update) or ADD to it
        override = request.POST.get('override') == 'True'
        
        # Add/Update cart
        cart.add(product=product, quantity=quantity, override_quantity=override)
        
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', {'cart': cart})
