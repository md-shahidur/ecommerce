from django.urls import path
from front import views

app_name = 'front'

urlpatterns = [
    path('', views.index, name='home'),
    path('details/<int:item_id>', views.item_detail, name='item_detail'),
]
