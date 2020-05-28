import requests
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from django_plotly_dash import DjangoDash


def now_fetch():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(url)
    data_list = r.json()
    return data_list

def now_display():
    data_now = now_fetch()
    now_bpi = data_now['bpi']
    usd = now_bpi['USD']
    rate = usd['rate_float']
    return rate

