from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Sum, Count
from .models import Product, Category
from orders.models import Order
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from accounts.models import Notification
# Helper to check if user is admin/staff
def is_admin(user):
    return user.is_staff

# --- PUBLIC VIEWS ---
def product_list(request):
    category_id = request.GET.get('category')
    products = Product.objects.filter(available=True)
    if category_id:
        products = products.filter(category_id=category_id)
    categories = Category.objects.all()
    return render(request, 'products/product_list.html', {'products': products, 'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

# --- MANAGER DASHBOARD & CRUD ---

@login_required
@user_passes_test(is_admin)
def manager_dashboard(request):
    # 1. Calculate Stats
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    # Calculate total revenue from all orders
    # (Simple logic: Sum of all order item totals - requiring loop or complex query)
    # For simplicity in this demo, we'll just count orders.
    
    recent_orders = Order.objects.order_by('-created_at')[:5]
    all_products = Product.objects.all().order_by('-id')

    context = {
        'total_products': total_products,
        'total_orders': total_orders,
        'recent_orders': recent_orders,
        'all_products': all_products,
    }
    return render(request, 'products/manager_dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Add New Product'})

@login_required
@user_passes_test(is_admin)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'title': 'Edit Product'})

@login_required
@user_passes_test(is_admin)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('manager_dashboard')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

@login_required
@user_passes_test(is_admin)
def update_order_status(request, order_id, status):
    """
    Admin clicks a button to change status.
    Status options: 'paid', 'shipped'
    """
    order = get_object_or_404(Order, id=order_id)
    
    if status == 'paid':
        order.paid = True
        order.save()
        # SEND NOTIFICATION
        Notification.objects.create(
            user=order.user,
            message=f"Order #{order.id} has been marked as PAID. We are processing it now."
        )
        messages.success(request, f"Order #{order.id} marked as Paid.")
        
    elif status == 'shipped':
        # (Assuming you might add a 'shipped' field later, but for now we just notify)
        Notification.objects.create(
            user=order.user,
            message=f"Good news! Order #{order.id} has been received/shipped."
        )
        messages.success(request, f"Notification sent for Order #{order.id}.")

    return redirect('manager_dashboard')