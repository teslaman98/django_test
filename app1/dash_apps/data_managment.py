import sqlite3
import datetime
import pandas as pd
from ..dash_apps import count_it

# c.execute("""CREATE TABLE assets (
#     net integer,
#     cash integer,
#     num_auth integer
#     )""")
#
# conn.commit()
#
# c.execute("""CREATE TABLE owned_stocks_port (
#     named text,
#     bought_price integer,
#     num_owned integer,
#     timez integer
#     )""")
#
# conn.commit()

"""    Manages the insertion of values into TABLE assets, owned_stocks_port    """


def asset_adding(net, cash):
    conn = sqlite3.connect('stock_value.db')
    c = conn.cursor()
    c.execute("INSERT INTO assets (net, cash, num_auth) VALUES (?,?,?)", (net, cash, datetime.datetime.now()))
    conn.close


def owned_stock_adding(named, price, num_owned):
    conn = sqlite3.connect('stock_value.db')
    c = conn.cursor()
    c.execute("INSERT INTO owned_stocks_port (named, bought_price, num_owned, timez) VALUES (?,?,?,?)",
              (named, price, num_owned, datetime.datetime.now()))
    conn.close

    def cash_transaction(amount):
        conn = sqlite3.connect('stock_value.db')
        c = conn.cursor()
        c.execute("INSERT INTO assets (net, cash, num_auth) VALUES (?,?,?)", (net, amount, datetime.datetime.now()))
        conn.close

# c.execute("DELETE FROM assets WHERE cash = 2")
