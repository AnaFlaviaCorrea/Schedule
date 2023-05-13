from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/logout/', views.logout, name='logout')
    
]