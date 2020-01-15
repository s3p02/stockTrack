from yahoo_fin import stock_info as si
import time
import sys
from datetime import datetime
from flask import escape


def stock_tracker(request):
    def get_price(stock_name):
        r = si.get_quote_table(stock_name, dict_result=False)
        print("stock_tracker stock_tracker {}".format(stock_name))
        stockPrice = r.loc[15]['value']
        print("stock_tracker stock_tracker {}".format(stockPrice))
        return stockPrice
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'stock_name' in request_json:
        stock_name = request_json['stock_name']
        print("stock_tracker stock_name request_json {}".format(stock_name))
    elif request_args and 'stock_name' in request_args:
        stock_name = request_args['stock_name']
        print("stock_tracker stock_name request_args {}".format(stock_name))
    else:
        stock_name = 'dis'
    stock_price = get_price(stock_name)
    print("stock_tracker stock_name stock_price {}".format(stock_price))
    return 'Hello {0} price is {1}!'.format(escape(stock_name), stock_price)
