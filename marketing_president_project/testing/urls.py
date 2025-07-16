from django.urls import path
from . import views

urlpatterns = [
    path('', views.testing_home, name='testing_home'),
]
