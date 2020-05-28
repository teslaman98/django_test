import dash
import dash_core_components as dcc
import dash_html_components as html
import requests
import pandas as pd
import json
import csv
import matplotlib.pyplot as plt
import numpy as np
from django_plotly_dash import DjangoDash
from dash.dependencies import Output, Input
from datetime import datetime

def STONKS_hourly():
    API_key = '&api_key={500d53d1a64c23b76a0b6494d9e0126803f039a84af46cc868d987b4ae052a4c}'
    link = 'https://min-api.cryptocompare.com/data/v2/histohour?fsym=BTC&tsym=USD&limit=10'
    url = link + API_key
    data_list = pd.read_json(url)
    # data_list.set_index('timestamp', inplace = True)
    return data_list

def STONKS_now():
    API_key = '&api_key={500d53d1a64c23b76a0b6494d9e0126803f039a84af46cc868d987b4ae052a4c}'
    link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    url = link + API_key
    data_list = pd.read_json(url)
    return data_now


app = DjangoDash('test_it')  # replaces dash.Dash

app.layout = html.Div([
    html.Div([dcc.Input(id="stock-input", value="", type="text")
              ]),


    html.Div([
        dcc.Graph(
            id='example-graph',
            figure={

                'layout': {
                    'title': 'Hourly BTC Value'
                }
            }
        )

]),
])


def stock_value(csv, key):
    data_value = csv[key]
    return data_value

@app.callback(dash.dependencies.Output("example-graph", "figure"),
              [dash.dependencies.Input("stock-input", "value")]
              )
def update_fig(input_value):
    stock = STONKS_hourly()
    second = stock['Data']
    third = second['Data']
    close = []
    time_list = []
    time_ref = []
    for hour in third:
        time_list.append(hour['time'])
    for hour in third:
        close.append(hour['close'])
    for x in time_list:
        time_ref.append(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    ticker = close
    time = time_ref
    data = [{'x': time, 'y': ticker, 'type': 'line', 'name': 'SF'}]
    return {
        "data": data
    }
