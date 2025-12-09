from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    
    # Manager URLs
    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('add/', views.product_create, name='product_create'),
    path('edit/<int:pk>/', views.product_update, name='product_update'),
    path('delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('order/update/<int:order_id>/<str:status>/', views.update_order_status, name='update_order_status'),
    
]