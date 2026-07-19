from django.urls import path
from . import views

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('create/', views.destination_create, name='destination_create'),
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('<int:pk>/edit/', views.destination_update, name='destination_update'),
    path('<int:pk>/delete/', views.destination_delete, name='destination_delete'),
    path('history/', views.destination_history, name='destination_history'),
    path('<int:pk>/restore/', views.destination_restore, name='destination_restore'),
]
