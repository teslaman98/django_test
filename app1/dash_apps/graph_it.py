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

def STONKS_csv(symbol, interval):
    API_key = 'FGZ5VI2OU5B413FO'
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=' + interval + "&outputsize=full&apikey=" + API_key + "&datatype=csv"
    data_list = pd.read_csv(url)
    # data_list.set_index('timestamp', inplace = True)
    return data_list



app = DjangoDash('graph_it')  # replaces dash.Dash

app.layout = html.Div([
    html.Div([dcc.Input(id="stock-input", value="", type="text")
              ]),


    html.Div([
        dcc.Graph(
            id='example-graph',
            figure={

                'layout': {
                    'title': 'Dash Data Visualization'
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
    stock = STONKS_csv(input_value, '5min')
    print (stock)
    ticker = stock['high']
    time = stock['timestamp']
    data = [{'x': time, 'y': ticker, 'type': 'line', 'name': 'SF'}]
    return {
        "data": data
    }
