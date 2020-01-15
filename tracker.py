import logging
from yahoo_fin import stock_info as si
import time
import sys
from datetime import datetime
from flask import escape


def stock_tracker(request):
    def get_price(stock_name):
        r = si.get_quote_table(stock_name, dict_result=False)
        stockPrice = r.loc[15]['value']
        return stockPrice
    request_json = request.get_json(silent=True)
    request_args = request.args
    if request_json and 'stock_name' in request_json:
        stock_name = request_json['stock_name']
    elif request_args and 'stock_name' in request_args:
        stock_name = request_args['stock_name']
    else:
        stock_name = 'chtr'
    stock_price = get_price(stock_name)
    return 'Hello {0} price is {1}!'.format(escape(stock_name), stock_price)
