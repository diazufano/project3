from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name ="login"),
    path("client",views.client, name = "client"),
    path("register",views.client, name = "register")
]
