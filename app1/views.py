from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from app1.dash_apps import graph_it
from app1.dash_apps import test_mk1
from app1.dash_apps import count_it
from app1.dash_apps.blockchain import now_display
from .forms import HomeForm
from .forms import HomeForm_two
from django.views.generic import TemplateView
from app1.models import Buy
from app1.dash_apps import blockchain

from django.db.models import Max
# from app1.models import Assets


##### Main Pages #####

def charts(requests):
    return render(requests, 'pages\\index.html', {})


def dashboard(request):
    stocks = blockchain.now_display()
    click = count_it.click_test()
    args = {"stocks": stocks}
    return render(request, 'pages\\dashboard.html', args)


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


class TableView(TemplateView):
    template_name = 'pages/tables.html'

    def get(self, request):
        form = HomeForm
        transactions = Buy.objects.all()
        cash = (len(transactions), transactions[len(transactions) - 1].cash)
        recent = cash[1]
        btc = (len(transactions), transactions[len(transactions) - 1].btc)
        recent_btc = btc[1]
        re_price = (len(transactions), transactions[len(transactions) - 1].price)
        re_pri_re = re_price[1]
        rec_net = now_display()
        trange = transactions[::-1]
        range_list = []
        for x in range(1, len(trange), 2):
            range_list.append(trange[x])

        args = {'form': form, 'transactions': transactions, 'recent': recent,
                'recent_btc': recent_btc, 'recent_net': rec_net,
                'range': range_list
                }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            number = form.cleaned_data['Buy_cash']
            form = HomeForm

        transactions = Buy.objects.all()
        cashonhand = (len(transactions), transactions[len(transactions)-2].cash)
        recent = cashonhand[1]
        bought = (len(transactions), transactions[len(transactions) - 1].Buy_cash)
        bought_re = bought[1]
        btc = (len(transactions), transactions[len(transactions) - 2].btc)
        recent_btc = btc[1]
        re_price = (len(transactions), transactions[len(transactions) - 1].price)
        re_pri_re = re_price[1]
        rec_net = now_display()
        trange = transactions[::-1]




        if float(bought_re) <= float(recent):
            if float(bought_re) >= 0:
                x = Buy(cash=(float(recent) - float(bought_re)),
                        btc=(float(recent_btc) + (float(bought_re)/float(re_pri_re))))
                x.save()
            else:
                x = Buy(cash=(float(recent) - float(bought_re)),
                        btc=(float(recent_btc) + (abs(float(bought_re)) / float(re_pri_re)) * -1 ))
                x.save()

        else:
            print ("error")


        return redirect('tables')
        args = {'form': form, 'transactions': transactions, 'recent':recent,
                'recent_btc':recent_btc, 'recent_net':rec_net,
                'range':trange, 'r': r
                }
        return render(request, self.template_name, args)


#### Registration/Login #####

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {"form": form})
