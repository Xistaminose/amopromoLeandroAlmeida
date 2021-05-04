from django.shortcuts import render
from rest_framework import viewsets
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.db.models import Q, Max


from .serializers import flightSerializer
from .models import flight
from airports.models import airports

class flightViewSet(viewsets.ModelViewSet):
    queryset = flight.objects.all().order_by('distance')
    serializer_class = flightSerializer

        

class OrderListJson(BaseDatatableView):
    model = flight

    def get_initial_queryset(self):
        return flight.objects.filter()
    
    columns = ['departure', 'arrival', 'distance', 'price', 'time', 'aircraft']
    order_columns = ['departure.iata', 'arrival.iata','distance', 'price', 'time', 'aircraft']
    max_display_length = 500

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(departure__iata__startswith=search)|
                            Q(arrival__iata__startswith=search)|
                            Q(price__startswith=search))
        return qs

    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            id = item.id
            json_data.append([
                escape(item.departure),
                escape(item.arrival),
                escape(round(item.distance,2)),
                escape(round(item.price,2)),
                escape(item.time),
                escape(item.aircraft),
            ])
        return json_data


def homepage(request):
    return render(request,'homepage.html')


def list_30(request):
    aeroporto = airports.state_with_most_airports()
    top_30 = flight.get_top_n_time(30)
    return render(request, 'list_30.html',{'top_30': top_30,'state':aeroporto[0]})

def list_airports_distance(request):
    aeroportos = airports.objects.distinct()
    my_object = []
    for i in aeroportos:
        x = flight.objects.filter(departure=i).order_by('-distance')
        my_object.append({'airport':i,
                        'distant':x.first(),
                        'near': x.last()})

    return render(request,'list_airports.html',{'airports':my_object})
