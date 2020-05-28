from django.db import models
from django.contrib.auth.models import User
from app1.dash_apps.blockchain import now_display
# from app1.dash_apps.test_mk1 import STONKS_now




# Create your models here.
#
bt_price = float(now_display())
# bt_1 = STONKS_now()
# print (bt_1)

class Buy(models.Model):
    Buy_cash = models.DecimalField(default=0, max_digits=24, decimal_places=8)
    buy_btc = models.DecimalField(default=0, max_digits=24, decimal_places=8)
    date = models.DateTimeField(auto_now=True)
    price = models.DecimalField(default=bt_price, max_digits=14, decimal_places=4)
    btc = models.DecimalField(default=0, max_digits=24, decimal_places=8)
    cash = models.DecimalField(default=10000.00, max_digits=24, decimal_places=8)

"""
class Assets(models.Model):
    btc = models.DecimalField(default=0.0, max_digits=14, decimal_places=4)
    cash = models.DecimalField(default=10000.0, max_digits=24, decimal_places=4)
"""
