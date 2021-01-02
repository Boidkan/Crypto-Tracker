# Crypto-Tracker
Simple script for tracking daily changes in crypto assets.

This scipt will continuously run and will generate and updated a csv file with prices for your crypto assets over time.


## Config.json

This script expect to have a Config.json file in the same directory. This is what data it expects:

```{
  "key": "YOUR_API_KEY",
  "crypto": {
    "ETH": 4.123,
    "BTC": 20.88,
    "LINK": 13.82,
    "LTC": 213
  },
  "frequency_seconds": 246060
}
```

The API key is for pro-api.coinmarketcap.com. You can get one for free.

'crypto` is a dictionary with crypto abbreviation and your holding amount for that asset as the key value pairs.
The script expects the crypto asset abbreviations to be capitalized. 

The `frequency_seconds` is how often you want it to check prices and write to the csv file.

