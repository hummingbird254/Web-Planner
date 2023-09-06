from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path("login/home/", views.home, name="user-home"),
    path("register/", views.register, name="register"),
    path("activity/<int:pk>/", views.details, name="detail"),
]
