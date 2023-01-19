from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    
    #Routes for cars index
    path('cars/', views.cars_index, name='index'),

    #Routes for car detail page
    path('cars/<int:car_id>/', views.cars_detail, name='detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_maint/', views.add_maint, name='add_maint'),
    path('cars/<int:car_id>/assoc_part/<int:part_id>/', views.assoc_part, name='assoc_part'),

    #Routes for Toys
    path('parts/', views.PartList.as_view(), name='parts_index'),
    path('parts/<int:pk>/', views.PartDetail.as_view(), name='parts_detail'),
    path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='parts_update'),
    path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='parts_delete'),   
]