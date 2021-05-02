import requests
from requests.auth import HTTPBasicAuth
import datetime
import time
from collections.abc import Mapping
from math import radians, cos, sin, asin, sqrt
from itertools import islice
import pandas as pd

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def nested_dict_iter(nested):
    for key, value, in nested.items():
        if isinstance(value, Mapping):
            for inner_key, inner_value, in nested_dict_iter(value):
                yield inner_key, inner_value
        else:
            yield key, value

def aeronaves(departure_airport,departure_date,arrival_airport):
    value = requests.get('http://stub.2xt.com.br/air/search/qhjvlDvYOwbbu9yq9Dq9DpfCqEbqWfvO/'+departure_airport+'/'+arrival_airport+'/'+departure_date,
                        auth=HTTPBasicAuth('leandroalmeida','tefvlD'))

    if value.json()['options']:
        return pd.DataFrame(value.json()['summary']),(value.json()['options'])


def haversine(lon1, lat1, lon2, lat2):
    import numpy as np

    
    # unpack the values for convenience
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km



def get_airports():
    return requests.get("http://stub.2xt.com.br/air/airports/qhjvlDvYOwbbu9yq9Dq9DpfCqEbqWfvO",
                        auth=HTTPBasicAuth('leandroalmeida','tefvlD')).json()





# #print(airports)
# today = datetime.datetime.now()
# #nests = nested_dict_iter(airports)
# x = (pd.DataFrame(airports.items()))


# for index, row in x.iterrows():
#     print(row[0],row[1])


# m = 0
# n = 0
# for i in airports:
#     n = n + 1
#     departure_airport = i
#     for j in airports:
#         arrival_airport = j
#         print(i,j)

#         departure_date = str((today + datetime.timedelta(days = 40)).date())
#         value = requests.get('http://stub.2xt.com.br/air/search/qhjvlDvYOwbbu9yq9Dq9DpfCqEbqWfvO/'+departure_airport+'/'+arrival_airport+'/'+departure_date,
#         auth=HTTPBasicAuth('leandroalmeida','tefvlD'))
#         #print(value.json()) 
#         x = (pd.DataFrame(value.json().items()))
#         print(x)
#         for index, row in x.iterrows():
#             print(row[0],row[1])
#             time.sleep(5)

#         # print('--------------------------------------/n')
#         # print(haversine(airports[i]['lon'],airports[i]['lat'],airports[j]['lon'],airports[j]['lat']))
#         # print(airports[i], airports[j])
#         # if value.json()['options']:
#         #     for k in value.json()['options']:
#         #         print(k['aircraft'])
#         # time.sleep(2)
#         # m = m + 1
#         # print(m)

# print(m,n)