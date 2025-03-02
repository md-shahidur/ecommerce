from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),
    path('details/<int:order_id>', views.order_detail, name='order_detail'),
    path('orders/', views.all_orders, name='all_orders'),
    path('test/', views.testpage, name='testpage'),


]
