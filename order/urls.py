from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('place_order/', views.place_order, name='place_order'),
    path('test/', views.testpage, name='testpage'),


]
