from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('', views.order_summery, name='order_summery'),


]
