from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('<int:user_id>/', views.cart_detail, name='cart_detail'),
    path('add/', views.cart_add, name='cart_add'),
    path('delete/', views.cart_delete, name='cart_delete'),
    path('update/', views.cart_update, name='cart_update'),
]
