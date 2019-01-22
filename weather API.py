# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:09:42 2019

@author: t.bowling
"""

import requests
import json
from datetime import date, timedelta
import pandas as pd

d1 = date(2017, 5, 1)
d2 = date(2017, 9, 20)

delta = d2 - d1         # timedelta
API_Key = "your-api-key-here"
#get one by signing up for 60 day trial here https://api.worldweatheronline.com

date_list = []
max_list = []
min_list = []
precip_list = []

for i in range(delta.days + 1):
    str_date = d1 + timedelta(i)
    PARAMS = {'key':API_Key,
              'q' :'40.99,29.13',
              'date' : str_date,
              'format' : 'json'}

    response = requests.get(url="https://api.worldweatheronline.com/premium/v1/past-weather.ashx", params = PARAMS)


    weather_data = response.json()
    weather_data2 = weather_data['data']['weather']
  

    weather_data2 = weather_data2[0]
    date_list.append(weather_data2['date'])
    max_list.append(weather_data2['maxtempC'])
    min_list.append(weather_data2['mintempC'])
    
    precip = 0.0
    for i in weather_data2['hourly']:
        precip += float(i['precipMM'])
    
    precip_list.append(precip)
    
final_weather_data = pd.DataFrame({'date': date_list,
                                   'Max_Temp': max_list,
                                   'Min_Temp': min_list,
                                   'Precipitation': precip_list})

final_weather_data.to_csv('weather_data.csv', index = False)
