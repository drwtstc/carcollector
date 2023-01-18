from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    #Routes for cars index
    path('cars/', views.cars_index, name='index'),


    #Routs for car detail page
]