from yahoo_fin import stock_info as si
import time
import sys
from datetime import datetime
from flask import escape
from google.cloud import logging


def stock_tracker(request):
    logging_client = logging.Client()
    log_name = 'my-log'
    logger = logging_client.logger(log_name)

    def get_price(stock_name, lc=logging_client):
        log_name_if = 'my-get_price'
        logger = lc.logger(log_name)
        r = si.get_quote_table(stock_name, dict_result=False)
        message1 = log_name_if+" stock_name {}".format(stock_name)
        logger.log_text(message1)
        print(message1)
        stockPrice = r.loc[15]['value']
        message2 = log_name_if+" stockPrice {}".format(stockPrice)
        logger.log_text(message2)
        print(message2)
        return stockPrice
    request_json = request.get_json(silent=True)
    request_args = request.args
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
    stock_price = get_price(stock_name)
    msgf = "stock_tracker stock_name stock_price {}".format(stock_price)
    logger.log_text(msgf)
    print(msgf)
    return 'Hello {0} price is {1}!'.format(escape(stock_name), stock_price)
