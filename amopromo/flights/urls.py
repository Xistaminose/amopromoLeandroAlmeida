from django.urls import include, path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^my/datatable/data/$', views.OrderListJson.as_view(), name='order_list_json'),
    path('',views.homepage, name="flight_list"),
    path('list30/',views.list_30, name="flight_list_30"),
    path('list_airports/',views.list_airports_distance, name="list_airports_distance")
]