from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path('activity/', views.activity, name='activity_detail'),
    path("login/user/", views.user, name="user"),

    path("register/", views.register, name="register"),
]
