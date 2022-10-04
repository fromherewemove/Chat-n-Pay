from django import views
from django.urls import path
from .views import signup

urlpatterns = [
    path("signup/", signup, name="signup")
]
