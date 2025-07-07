from django.urls import path
from . import views

urlpatterns = [
    path('', views.funnel_home, name='funnel_home'),
]
