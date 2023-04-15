import datetime
from time import sleep

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from users.forms import NewUserForm

from real_state.mongodb import mongodb


def set_cookie(response, key, value, days_expire=7):
    one_day = 24 * 60 * 60
    max_age = days_expire * one_day if days_expire is not None else one_day

    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            response = redirect("home")
            set_cookie(response, "user_id", str(request.user.id))
            login(request, user)
            messages.success(request, "Registration successful.")
            sleep(0.3)
            return response

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
                response = redirect("home")
                set_cookie(response, "user_id", str(request.user.id))
                messages.info(request, f"You are now logged in as {username}.")
                return response
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")
    form = AuthenticationForm()
    return render(
        request=request, template_name="login.html", context={"login_form": form}
    )


def homepage(request):
    estates = mongodb.filter_estates({})
    context = {
        "estates": list(estates),
        "title": "Pending Estate Title",
        "description": "Pending Estate Description",
        "coordinates": "Pending Estate Coordinates",
    }
    return render(request=request, template_name="home.html", context=context)


def logout_request(request):
    response = redirect("home")
    logout(request)
    response.delete_cookie("user_id")
    messages.info(request, "You have successfully logged out.")
    return response
