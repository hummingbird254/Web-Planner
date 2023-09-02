from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import ToDoList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView


# Create your views here.
def home(request):
    return render(request, "main/home.html", {})


@login_required()
def activity(request, activity_id):
    return render(request, "main/post_detail.html", {})


@login_required
def user(request):
    username = request.user
    if request.method == "POST":

        if request.POST.get("save"):
            for activity in username.todolist.all():
                activity.save()
        elif request.POST.get("newToDoList"):
            name = request.POST.get("newActivity")
            if len(name) > 2:
                ToDoList.objects.create(user=username, name=name)
            else:
                pass
    return render(request, "main/user.html", {"username": username})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/user")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


class ToDoListDetails(DetailView):
    model = ToDoList

