from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from accounts.forms import LoginForm


def user_login(request):
    if request.method == "GET":
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request, user)
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)
