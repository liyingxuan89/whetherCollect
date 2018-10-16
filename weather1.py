import requests
from pprint import pprint
import json
from pandas.io.json import json_normalize
import pandas as pd

year = range(2001,2018)
date = [str(y)+'0101'+str(y)+'1231'for y in year]


Stationid = ["56294","56196","58122","56492","57516","57411"]

def weather(date,stationid):
    url = "https://api-ak.wunderground.com/api/f9caff179aa553f4/history_"+ date +"/lang:EN/units:english/bestfct:1/v:2.0/q/" + "zmw:00000.1." + str(stationid) + ".json?showObs=0&ttl=120"
    data = requests.get(url).json()   
    df = json_normalize(data['history']['days']).rename(columns=lambda x: x.replace('summary.',''))
    return df

def weather_city(stationid):
    return pd.concat([weather(dat,stationid) for dat in date])



print weather(Stationid[-1], date[0])

#df = [weather_city(stat) for stat in stationid]
#    
#writer = pd.ExcelWriter('weather.xlsx')
#for i, d in enumerate(df):
#    d.to_excel(writer,sheet_name="{0}".format(city[i]))
#writer.save()

