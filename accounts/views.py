from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .forms import UserUpdateForm
from .models import Notification

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! Please login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)

    # 2. Fetch Data
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    
    # 3. Mark notifications as read (Optional logic, or do it via a button)
    # notifications.update(is_read=True) 

    context = {
        'orders': orders,
        'user_form': user_form,
        'notifications': notifications
    }
    return render(request, 'accounts/profile.html', context)