import requests
import json
import csv

#Print a json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#Another api, give current weather
#Resp = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=93117,us&APPID=19dde4efd89c2d1f28cec84f9688b2d5")

#Resp = requests.get("https://www.ncei.noaa.gov/access/services/data/v1?dataset=global-marine&dataTypes=WIND_DIR,WIND_SPEED&stations=AUCE&startDate=2016-01-01&endDate=2016-01-02&boundingBox=90,-180,-90,180")
#Resp = requests.get("https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&dataTypes=DP01,DP05,DP10,DSND,DSNW,DT00,DT32,DX32,DX70,DX90,SNOW,PRCP&stations=ASN00084027&startDate=2000-01-01&endDate=2001-01-01&includeAttributes=true&format=json")
#Resp = requests.get("https://www.ncei.noaa.gov/access/services/data/v1?dataset=daily-summaries&stations=USC00041253&startDate=2019-10-01&endDate=2019-10-10&format=csv");


#Currently set for some weather station in Lake Cachuma, asks for rain and temp
parameters = {
    "dataset" : "daily-summaries",
    "stations" : "USC00041253",
    "startDate" : "2018-10-10",
    "endDate" : "2019-10-29",
    "dataTypes" : "PRCP,TMAX,TMIN",
    "includeStationName" : "true",
    "units" : "metric",
    "format" : "csv"
}

Resp = requests.get("https://www.ncei.noaa.gov/access/services/data/v1?", params = parameters);

"""
#To print response, only if response was a JSON
jprint(Resp.json())
"""

a = Resp.content.decode('utf-8')
cr = csv.reader(a.splitlines(), delimiter=',')
melist = list(cr)

with open('WeatherData.csv', mode = 'w') as W_file:
    W_writer = csv.writer(W_file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    for row in melist:
        W_writer.writerow(row)


