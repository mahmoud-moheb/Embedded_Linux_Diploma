#!/usr/bin/python3
#this is code shows current bitcoin rate vs usd 
import requests
data=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
dic=data.json()
print("1 Bitcoin is equal to: {} USD".format(dic["bpi"]["USD"]["rate_float"]))