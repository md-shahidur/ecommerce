from django.urls import path
from members import views

app_name = 'members'

urlpatterns = [
    path('login/', views.member_login, name='login'),
    path('signup/', views.member_signup, name='signup'),
    path('profile/<int:user_id>', views.profile_page, name='profile'),
    path('edit_profile/<int:data_id>', views.edit_profile, name='edit_profile'),

]
