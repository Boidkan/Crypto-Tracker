import requests
import json
from datetime import datetime
from math import ceil

class RequestManager:
    def getPrices():
    
        file = open("Config.json")
        config = json.load(file)
        
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

        return (titles, values)
