from utils import take, haversine, get_airports
import pandas as pd
import datetime
import requests
from requests.auth import HTTPBasicAuth
import time


airports = get_airports()
df = pd.DataFrame.from_dict(airports,orient='index')
distances = pd.DataFrame()
aeronave = pd.DataFrame()

def aircraft_values(data, distance):

    departure_time = datetime.datetime.strptime(data.departure_time, '%Y-%m-%dT%H:%M:%S')
    arrival_time = datetime.datetime.strptime(data.arrival_time, '%Y-%m-%dT%H:%M:%S')
    timediff = ((arrival_time - departure_time).seconds / 3600.00)
    velocity = float(distance/timediff)
    fare_price = data.fare_price
    aircraft = data.aircraft
    farekm = float(fare_price/distance)
    

def seriess(data, iata1):
    pd.Series(index = data.index, data = [get_data(data.iloc[i], data.lon[iata1], data.lat[iata1],iata1) for i in range(len(data.index))])

def get_data(data, lon1, lat1,iata1):
    iata2 = data.iata
    if iata1 != iata2:
        lat2 = data.lat
        lon2 = data.lon
        iata = data.iata
        distance = haversine(lon1,lat1,lon2,lat2)
        value = requests.get('http://stub.2xt.com.br/air/search/qhjvlDvYOwbbu9yq9Dq9DpfCqEbqWfvO/'+iata1+'/'+iata2+'/'+departure_date,
                                auth=HTTPBasicAuth('leandroalmeida','tefvlD'))
        options = pd.DataFrame(value.json()['options'])
        return options.apply(lambda column: aircraft_values(column,distance), axis=1)   

today = datetime.datetime.now()
departure_date = str((today + datetime.timedelta(days = 40)).date())


df2 = pd.DataFrame(index = df.index, columns = df.index)
for i in df2.columns:
    now = datetime.datetime.now()
    df2[i] = seriess(df,i)
    after = datetime.datetime.now()
    print(after-now)


# for i in df.index:
#     df.apply(lambda column: get_data(column,df.lon[i],df.lat[i],i),axis=1)






