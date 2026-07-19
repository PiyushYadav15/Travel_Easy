# hotels/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('hotels/', views.hotel_list, name='hotel_list'),
    path('hotels/create/', views.hotel_create, name='hotel_create'),
    path('hotels/<int:pk>/', views.hotel_detail, name='hotel_detail'),
    path('hotels/<int:pk>/update/', views.hotel_update, name='hotel_update'),
    path('hotels/<int:pk>/delete/', views.hotel_delete, name='hotel_delete'),
    path('hotels/history/', views.hotel_history, name='hotel_history'),
    path('hotels/<int:pk>/restore/', views.hotel_restore, name='hotel_restore'),
]
