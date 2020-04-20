import requests
import re
import os
from dotenv import load_dotenv
load_dotenv()
apiKey = os.getenv("google_apiKey")

# function to get info from Google API
def getFromGoogle(queryParams=dict()):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    res = requests.get(url, params=queryParams)
    print(res.status_code)
    return res.json()

# function to generate query params for the API request
def getQueryParams(radius,tipo,keyword,pagetoken):
    return {"location":"37.774929,-122.4194183",
    "radius":radius,
    "type":tipo,
    "keyword":keyword,
    "key":f'{apiKey}',
    "pagetoken":pagetoken}

# function to generate a list with info from API response
def getInfoFromRes(res,check,name):
    lista_local = []
    for e in res["results"]:
        if re.search(check, e["name"]):
            lista_local.append({"category":name,"name":e["name"],
                           "location":{"type":"Point","coordinates":[e["geometry"]["location"]["lng"],e["geometry"]["location"]["lat"]]}})
    return lista_local
