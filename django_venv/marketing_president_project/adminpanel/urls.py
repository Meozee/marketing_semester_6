from django.urls import path
from . import views

urlpatterns = [
    path('navbar/', views.admin_navbar, name='admin_navbar'),
    path('', views.admin_panel, name='admin_panel'),
]
