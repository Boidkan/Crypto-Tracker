# Crypto-Tracker
Simple script for tracking daily changes in crypto assets


## Config.json

This script expect to have a Config.json file in the same directory. This is what data it expects:

```{
  "key": "YOUR_API_KEY",
  "crypto": {
    "ETH": 4,
    "BTC": 20,
    "LINK": 13,
    "LTC": 213
  }
}
```

The api key is for pro-api.coinmarketcap.com. You can get one for free. It expect the crypto asset abbreviations to be capitalized. 
The number valye for each crypo abreviation is the amount you have or wish for the script to compute.

