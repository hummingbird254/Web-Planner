from django.urls import path
from . import views
from .views import ToDoListDetails

urlpatterns = [
    path('', views.home, name='home'),
    path("home/", views.home, name="home"),
    path("todolist/<int:pk>/", ToDoListDetails.as_view(), name="activity-details"),
    path('activity/', views.activity, name='activity_detail'),
    path("login/user/", views.user, name="user"),

    path("register/", views.register, name="register"),
]
