import pandas as pd
import datetime
import time
import aiohttp
import asyncio

from utils import haversine, get_airports


async def save_airports(i, data, session):
    myobjpost = {
                    "name": data[i].city,
                    "iata": data[i].iata,
                    "lat": data[i].lat,
                    "lon": data[i].lon,
                    "state":data[i].state
                }
    apipost = 'http://127.0.0.1:8000/api/airports/'
    async with session.post(apipost, data=myobjpost) as response:
        await response.text()

async def save(topost, session1):
    myobjpost = {"urlapi": topost[0],
                "distance": topost[1],
                "price": topost[2],
                "aircraft": topost[3],
                "departure": topost[4],
                "arrival": topost[5],
                "time": topost[6],
                }

    apipost = 'http://127.0.0.1:8000/api/flights/'
    async with session1.post(apipost, data=myobjpost) as response:
        await response.text()



def aircraft_values(data, distance, iata1, iata2, url_mockup):
    departure_time = datetime.datetime.strptime(data.departure_time, '%Y-%m-%dT%H:%M:%S')
    arrival_time = datetime.datetime.strptime(data.arrival_time, '%Y-%m-%dT%H:%M:%S')
    timediff = ((arrival_time - departure_time).seconds / 3600)
    velocity = float(distance/timediff)
    timediff = ((arrival_time - departure_time).seconds / 60)
    fare_price = data.fare_price
    aircraft = data.aircraft
    farekm = float(fare_price/distance)
    return url_mockup, distance, farekm, aircraft['model'], iata1, iata2, timediff

def opapply(options, distance, url_mockup, iata1, iata2):
    return (options.apply(lambda column: aircraft_values(column, distance, iata1, iata2, url_mockup), axis=1))

async def get_data_test(data1, data2, departure_date, session, df):
    iata1 = df[data1].iata
    iata2 = df[data2].iata
    if iata1 != iata2:  
        lat1 = df[data1].lat
        lat2 = df[data2].lat
        lon1 = df[data1].lon
        lon2 = df[data2].lon
        distance = haversine(lon1,lat1,lon2,lat2)
        url_mockup = 'http://stub.2xt.com.br/air/search/qhjvlDvYOwbbu9yq9Dq9DpfCqEbqWfvO/'+iata1+'/'+iata2+'/'+departure_date
        async with session.get(url_mockup, auth=aiohttp.BasicAuth('leandroalmeida','tefvlD')) as response:
            value = await response.json()
        options = pd.DataFrame(value['options'])
        if not options.empty:
            return opapply(options,distance, url_mockup, iata1, iata2)

async def main():    
    airports = get_airports()
    df = pd.DataFrame.from_dict(airports)
    today = datetime.datetime.now()
    total = datetime.datetime.now()
    departure_date = str((today + datetime.timedelta(days = 40)).date())
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in df:
            task = save_airports(i,df,session)
            tasks.append(task)
        await asyncio.gather(*tasks)

    async with aiohttp.ClientSession() as session:
        async with aiohttp.ClientSession() as session1:
            for i in df:
                now = datetime.datetime.now()
                tasks = [get_data_test(i,j,departure_date,session,df) for j in df]
                result = await asyncio.gather(*tasks)
                tasks_post = []
                for k in result:
                    if k is not None:
                        topost = k.min(axis=0)
                        taskpost = save(topost, session1)
                        tasks_post.append(taskpost)
                await asyncio.gather(*tasks_post)     
                print("airport: ",i ,"time: ", datetime.datetime.now() - now)
    print('total', datetime.datetime.now() - total)

if __name__ == '__main__':
    asyncio.run(main())
