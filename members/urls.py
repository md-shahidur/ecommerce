from django.urls import path
from members import views

app_name = 'members'

urlpatterns = [
    path('login/', views.member_login, name='login'),
    path('signup/', views.member_signup, name='signup'),

]
