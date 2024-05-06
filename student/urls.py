from django.urls import path ,include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/',views.logout_view, name = 'logout'),
    path('register/',views.register, name = 'register'),
   
]