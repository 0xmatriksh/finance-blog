import requests
import json

response = requests.get('https://newweb.nepalstock.com.np/api/nots/nepse-index',params=requests.request.GET)
json_data = response.json()
print(json_data)