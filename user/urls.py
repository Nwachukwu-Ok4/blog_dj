from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.userLogin, name="userLogin" ),
    path("signup/", views.userSignup, name="userSignup" ),
    path("logout/", views.userLogout, name="userLogout" ),
]