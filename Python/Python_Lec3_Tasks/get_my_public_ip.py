#!/usr/bin/python3
import requests
data=requests.get("https://api.ipify.org/?format=json")
ip=data.json()
print("your public ip is: "+ip['ip'])
ipinfo="https://ipinfo.io/"+str(ip['ip'])+"/geo"
data=requests.get(ipinfo)
location=data.json()
print("your ip location is: "+location['loc'])