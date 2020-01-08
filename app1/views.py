from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.dash_apps import graph_it
from app1.dash_apps import test_mk1

##### Main Pages #####

def charts(requests):
    return render(requests, 'pages\index.html', {})

def dashboard(request):
    return render(request, 'pages\dashboard.html', {})






#### Registration/Login #####

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {"form":form})

