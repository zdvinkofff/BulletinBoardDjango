from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.home, name='home'),
    path('advertisements/', views.advertisement_list, name='advertisement_list'),
    path('advertisements/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('advertisements/add/', views.add_advertisement, name='add_advertisement'),
    path('advertisements/<int:pk>/edit/', views.edit_advertisement, name='edit_advertisement'),
]

