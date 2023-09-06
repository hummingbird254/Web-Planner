from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from .models import ToDoList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView


# Create your views here.
def home(request):
    return render(request, "main/home.html", {})


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
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(request, "register/register.html", {"form": form})


@login_required
def details(request, pk):
    activity = get_object_or_404(ToDoList, pk=pk)
    if request.method == "POST":

        if request.POST.get("save"):
            for item in activity.item_set.all():
                item.save()
        elif request.POST.get("newItem"):
            text = request.POST.get("newItemInput")
            if len(text) > 2:
                activity.item_set.create(text=text)
            else:
                pass
    return render(request, "main/detail.html", {"activity": activity})
