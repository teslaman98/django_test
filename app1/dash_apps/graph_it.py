
import os
from django_plotly_dash import DjangoDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas
import plotly.graph_objects as go




stock_list = ['TSLA', 'MSFT', 'AAPL']
time_int = ['5', '10', '30']

app = DjangoDash('graph_it')

labels1 = [['monkeys', 'elephants'],
          ['birds', 'dinosaurs'],
          ['unicorns', 'giraffes']]

values1 = [[50, 40],
          [100, 10],
          [100, 20]]

data = []

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='TPiePlot',
                  figure={
                      'data': [go.Pie(labels=labels1,
                                      values=values1,
                                      marker=dict( line=dict(color='#fff', width=1)),
                                      hoverinfo='label+value+percent', textinfo='value',
                                      domain={'x': [0, .25], 'y': [0, 1]}
                                      )
                               ],
                      'layout': go.Layout(title='T',
                                          autosize=True
                                          )
                  }
                  )
    ])
    ])
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

