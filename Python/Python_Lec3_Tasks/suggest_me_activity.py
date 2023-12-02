#!/usr/bin/python3
#this is code shows current bitcoin rate vs usd 
import requests
data=requests.get("https://www.boredapi.com/api/activity")
dic=data.json()
print("we suggest you to "+str(dic['activity']))