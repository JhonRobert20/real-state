from time import sleep

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from users.forms import NewUserForm


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            messages.success(request, "Registration successful.")
            sleep(0.3)
            return redirect("home")

        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(
        request=request, template_name="register.html", context={"register_form": form}
    )


def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )


def homepage(request):
    return render(request=request, template_name="home.html", context={})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("home")