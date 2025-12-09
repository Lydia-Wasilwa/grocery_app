from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        # In orders/views.py inside checkout()

        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            
            # --- SIMULATE PAYMENT ---
            order.paid = True  # <--- Add this line to mark as paid immediately
            # ------------------------

            order.save()
            # ... rest of the code ...
    else:
        form = OrderCreateForm()
    return render(request, 'orders/checkout.html', {'cart': cart, 'form': form})
