from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='/account/login', redirect_field_name='next')
def index(request):
    return HttpResponse("Account index.")


def login(request):
    if request.method == "GET":
        return render(request, 'account/login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    if username and password:
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect('/account/')

        messages.error(request, "Username or password is incorrect.")
    else:
        messages.error(request, "Username and password are required.")

    return render(request, 'account/login.html')







    return redirect('/account/')


def register(request):
    return HttpResponse("Register page.")
