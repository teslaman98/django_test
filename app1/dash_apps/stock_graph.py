import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import pandas as pd
import json
import csv
import matplotlib.pyplot as plt
import numpy as np



def STONKS_csv(symbol, interval):
    API_key = "FGZ5VI2OU5B413FO"
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+symbol+"&interval="+interval+"&outputsize=full&apikey="+API_key+"&datatype=csv"
    data_list = pd.read_csv(url)
    #data_list.set_index('timestamp', inplace = True)
    return data_list

def stock_value(csv, key):
    data_value = csv[key]
    return data_value

from django_plotly_dash import DjangoDash

app = DjangoDash('test_it')   # replaces dash.Dash

app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )

])

"""""""
AAPL = STONKS_csv("AAPL", '5min')
print (AAPL)
print ('hello world')