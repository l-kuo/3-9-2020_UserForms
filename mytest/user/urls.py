from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from .views import *

urlpatterns = [

    path ('register/',register,name='user-register'),
    path ('login/', auth_views.LoginView.as_view(template_name='user/login.html'),name = 'user-login'),
    path ('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name = 'user-logout'),
    path ('profile/',profile,name = 'user-profile')

]