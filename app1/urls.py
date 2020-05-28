from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from app1 import views
from . import views
from app1.views import TableView
from app1.dash_apps import graph_it



urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('charts', views.charts, name='charts'),
  path('tables', TableView.as_view(), name='tables'),
  path('transaction', views.get_name, name='get_name'),
]

