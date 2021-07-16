import requests
import json
import httpx

r = httpx.get('https://newweb.nepalstock.com.np/api/nots/nepse-index')
print(r.json())