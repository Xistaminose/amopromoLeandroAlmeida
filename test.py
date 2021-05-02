from utils import haversine, get_airports
import pandas as pd
import datetime
import requests
from requests.auth import HTTPBasicAuth
import time


airports = get_airports()
df = pd.DataFrame.from_dict(airports,orient='index')

def save_airports(data):
    myobjpost = {
                    "name": data.city,
                    "iata": data.iata,
                    "lat": data.lat,
                    "lon": data.lon
                }
    apipost = 'http://127.0.0.1:8000/api/airports/'
    y = requests.post(apipost, data = myobjpost)     

def save(data, url,iata1,iata2):
    print(url)
    x = (data.min(axis=0))
    #@print(x)
    print(x[3])
    myobjpost = {"urlapi": url,
                "distance": x[0],
                "price": x[1],
                "aircraft": x[2],
                "departure": iata1,
                "arrival": iata2,
                "time": x[3],
                }
    apipost = 'http://127.0.0.1:8000/api/flights/'
    y = requests.post(apipost, data = myobjpost)
    #print(x)
def aircraft_values(data, distance):
    departure_time = datetime.datetime.strptime(data.departure_time, '%Y-%m-%dT%H:%M:%S')
    arrival_time = datetime.datetime.strptime(data.arrival_time, '%Y-%m-%dT%H:%M:%S')
    timediff = ((arrival_time - departure_time).seconds / 3600.00)
    velocity = float(distance/timediff)
    timediff = ((arrival_time - departure_time))
    fare_price = data.fare_price
    aircraft = data.aircraft
    farekm = float(fare_price/distance)
    return (distance, farekm, aircraft['model'],timediff)


def get_data(data, lon1, lat1,iata1):
    iata2 = data.iata
    if iata1 != iata2:
        lat2 = data.lat
        lon2 = data.lon
        iata = data.iata
        distance = haversine(lon1,lat1,lon2,lat2)
        url_mockup = 'http://stub.2xt.com.br/air/search/qhjvlDvYOwbbu9yq9Dq9DpfCqEbqWfvO/'+iata1+'/'+iata2+'/'+departure_date
        value = requests.get(url_mockup,
                                auth=HTTPBasicAuth('leandroalmeida','tefvlD'))
        options = pd.DataFrame(value.json()['options'])
        if not options.empty:
            x = options.apply(lambda column: aircraft_values(column,distance), axis=1)  
            save(x,url_mockup,iata1,iata2)
         

today = datetime.datetime.now()
departure_date = str((today + datetime.timedelta(days = 40)).date())
df = df[:10]

#df.apply(lambda column: save_airports(column), axis=1)
for i in df.index:
    print(i)
    df.apply(lambda column: get_data(column,df.lon[i],df.lat[i],i),axis=1)
