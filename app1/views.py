from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.dash_apps import graph_it
from app1.dash_apps import test_mk1
from app1.dash_apps import count_it
from .forms import NameForm

##### Main Pages #####

def charts(requests):
    return render(requests, 'pages\\index.html', {})

def dashboard(request):
    money = count_it.current_money_display()
    net = count_it.current_net_display()
    #stocks = count_it.current_portfolio()
    click = count_it.click_test()
    return render(request, 'pages\\dashboard.html',
                  {"money" : money,
                   "net" : net,
                   # "stocks" : stocks
                   })
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'pages\\transaction.html', {'form': form})

def tables(request):
    return render(request, 'pages\\tables.html', {})






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

