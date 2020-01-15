import logging
from yahoo_fin import stock_info as si
import time
import sys
from influxdb import InfluxDBClient
from datetime import datetime


client = InfluxDBClient(host='localhost', port=8086)

NASDAQcode = str(sys.argv[1])

while True:
    data = []
    start_time = time.perf_counter()
    r = si.get_quote_table(NASDAQcode, dict_result = False)
    writeTime = datetime.utcnow()
    latency = time.perf_counter() - start_time
    stockPrice = r.loc[15]['value']
    print("--- %s ---" % (NASDAQcode))
    print("--- Latency %s seconds ---" % (latency))
    print(r)
    print(stockPrice)
    print("--- %s WriteTime ---" % (writeTime))
    data = [
        {
            "measurement": NASDAQcode,
            "tags": {
                "NASDAQcode": NASDAQcode
            },
            "time": writeTime,
            "fields": {
                "latency": latency,
                "stockPrice": stockPrice
            }
        }
    ]
    client.write_points(data, database='stockprices', time_precision='ms')
    data.clear()