import sqlite3
import datetime
import pandas as pd
from ..dash_apps import data_managment

"""
-stores the money left
-is accesable to delete the money
-is accesable to net the money

"""
conn = sqlite3.connect('stock_value.db')

c = conn.cursor()

"""  Get the bought price  """


def click_test():
    good = "<p> Pass </p>"
    return good


def buy_price(ticker):
    conn = sqlite3.connect('stock_value.db')
    c = conn.cursor()
    stock_test = "TSLA"
    named = "TSLA"
    price = 499
    num_owned = 21
    c.execute("SELECT bought_price, max(timez) FROM owned_stocks_port WHERE named=ticker")
    conn.commit()
    money = (c.fetchall())
    money_mrkI = money
    money_mrkII = money_mrkI
    return money_mrkI
    conn.close


def buy_num(ticker):
    conn = sqlite3.connect('stock_value.db')
    c = conn.cursor()
    stock_test = "TSLA"
    named = "TSLA"
    price = 499
    num_owned = 21
    c.execute("SELECT num_owned, max(timez) FROM owned_stocks_port WHERE named=ticker")
    conn.commit()
    money = (c.fetchall())
    money_mrkI = money
    money_mrkII = money_mrkI
    # return money_mrkII[0]
    return money_mrkI
    conn.close


"""  Value when bought  """


def bought_value():
    price = buy_price('TSLA')
    num = buy_num('TSLA')
    net = price * num
    return net


"""  Value Now """


def current_value(ticker):
    cur = STONKS_csv(ticker)
    net = cur - bought_value()
    return net


"""                                   API CALLS AND BREAKDOWN                                 """
# c.execute("INSERT INTO assets (net, cash, num_auth) VALUES (?,?,?)", (net, cash, num_auth) )

# conn.commit()
#
# c.execute("SELECT * FROM assets")
# print (c.fetchall)
#
"""  API call for CSV  """


def STONKS_csv(symbol):
    API_key = "FGZ5VI2OU5B413FO"
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + symbol + "&interval=5min&outputsize=full&apikey=" + API_key + "&datatype=csv"
    data_list = pd.read_csv(url)
    # data_list.set_index('timestamp', inplace = True)
    return data_list


"""  CSV breakdown for the current high price  """


def price_now(ticker):
    stock = STONKS_csv(ticker)
    high = stock['high']
    return high[0]


"""  **Likely old and outdated**  """


def net_now():
    old_price = 506
    new_price = price_now("TSLA")
    net_price = new_price - old_price
    return net_price


"""                                       DISPLAY FUNCTIONS                                   """


def current_money_display():
    """  Display most recent cash log  """
    conn = sqlite3.connect('stock_value.db')

    c = conn.cursor()
    t = 2
    net = 123
    cash = 5
    num_auth = datetime.datetime.now()
    conn.commit()
    c.execute("SELECT cash, max(num_auth) FROM assets")
    money = (c.fetchone())
    return money[0]
    conn.close


def current_net_display():
    """  Displays most recent log of net value of all stocks  """
    conn = sqlite3.connect('stock_value.db')

    c = conn.cursor()
    t = 2
    net = 123
    cash = 2
    num_auth = datetime.datetime.now()
    conn.commit()
    c.execute("SELECT net, max(num_auth) FROM assets")
    money = (c.fetchone())
    return money[0]
    conn.close


conn.close

# https://drive.google.com/drive/folders/1VOvtuV3oCavScCBnPs_SHl01ODdo74F8?usp=sharing
