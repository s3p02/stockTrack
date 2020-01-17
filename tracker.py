from yahoo_fin import stock_info as si
import time
import sys
from datetime import datetime
from flask import escape
from google.cloud import logging


def stock_tracker(request):
    """Stock Tracker function. Invoked by a request
    """
    logging_client = logging.Client()
    log_name = 'my-log'
    logger = logging_client.logger(log_name)
    """Logger invoked for monitoring in stack-driver
    """

    def get_price(stock_name, lc=logging_client):
        """Nested function that performs the stock price request. Given a stock_name, the function returns the stock price.
        """
        log_name_if = 'get_price'
        logger = lc.logger(log_name)
        start = time.time()
        r = si.get_quote_table(stock_name, dict_result=False)
        end = time.time()
        latency = end - start
        message1 = log_name_if+" stock_name {}".format(stock_name)
        logger.log_text(message1)
        print(message1)
        stockPrice = r.loc[15]['value']
        message2 = log_name_if+" stockPrice {}".format(stockPrice)
        logger.log_text(message2)
        print(message2)
        return (stockPrice,latency)
    request_json = request.get_json(silent=True)
    request_args = request.args
    """request_json & request_args are parsers for the requests taht come in
    """
    if request_json and 'stock_name' in request_json:
        stock_name = request_json['stock_name']
        msgi = "stock_tracker stock_name request_json {}".format(stock_name)
        logger.log_text(msgi)
        print(msgi)
    elif request_args and 'stock_name' in request_args:
        stock_name = request_args['stock_name']
        msgi = "stock_tracker stock_name request_args {}".format(stock_name)
        logger.log_text(msgi)
        print(msgi)
    else:
        stock_name = 'dis'
    """This is a conditional to parse the request and obtain the stock_name. By default the stock_name is dis
    """
    stock_price_latency = get_price(stock_name)
    stock_price = stock_price_latency[0]
    stock_latency = stock_price_latency[1]
    """From the obtained stock_name, the price is retrived using the get_price function"""
    msgf = "stock_tracker stock_name stock_price {}".format(stock_price)
    logger.log_text(msgf)
    print(msgf)
    fr = 'Hello {0} price is {1}! It took {2} seconds.'.format(escape(stock_name), stock_price, stock_latency)
    """fr is the final response returned by stock_tracker function.
    """
    return fr
