from urllib import response
import requests
import json
baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
# parameters = {'upc': '012993441012'}
parameters = {'upc': '885909950805'}
response = requests.get(baseURL,params=parameters)
# print(response.url)
content = response.content
# print(content)
info = json.loads(content)
# print(type(info))
# print(json.dumps(info,indent=2))
iteminfo = info['items'][0]
itemoffers = iteminfo['offers'][0]
title = iteminfo['title']
brand = iteminfo['brand']
price = itemoffers['price']
print(title)
print(brand)
print(price)