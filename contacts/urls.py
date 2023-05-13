from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('search/', views.search, name='search'),
    path('details/<int:id>', views.details, name = 'details'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('add/', views.add, name ='add'),
    path('edit/<int:id>', views.edit, name ='edit'),
    path('filter/', views.filter_contacts, name='filter'),
    
    
   
]