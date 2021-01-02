import requests
import json
from CSVManager import CSVManager
from datetime import datetime
from math import ceil
import sched, time

file = open("Config.json")
config = json.load(file)


scheduler = sched.scheduler(time.time, time.sleep)
timer = config["frequency_seconds"]

def addRow():

    key = config["key"]
    symbols = list(sorted(config["crypto"].keys()))

    params = ",".join(symbols)

    url = ' https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=' + params
    headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': key}

    request = requests.get(url, headers = headers)

    data = json.loads(request.text)

    total = 0
    date = datetime.today().strftime("%m/%d/%y")
    values = [date]

    for symbol in symbols:
        price = data["data"][symbol]["quote"]["USD"]["price"]
        amount = config["crypto"][symbol]
        value = ceil(amount * price * 100) / 100.0
        total += amount * price #Don't want to round total until everything is added up
        values += [value]

    total = ceil(total * 100) / 100.0
    values += [total]
    titles = [""] + symbols + ["TOTAL"]

    csv_manager = CSVManager()
    csv_manager.write(titles, values)

    print("Added:" + str(symbols))
    scheduler.enter(timer, 1, addRow)

scheduler.enter(0, 1, addRow)
scheduler.run()