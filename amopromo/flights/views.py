from django.shortcuts import render
from rest_framework import viewsets
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape
from django.db.models import Q

from .serializers import flightSerializer
from .models import flight

class flightViewSet(viewsets.ModelViewSet):
    queryset = flight.objects.all().order_by('distance')
    serializer_class = flightSerializer

class OrderListJson(BaseDatatableView):
    # The model we're going to show
    model = flight

    def get_initial_queryset(self):
        return flight.objects.filter()
    # define the columns that will be returned
    columns = ['urlapi', 'distance', 'price', 'aircraft', 'departure', 'arrival']

    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['distance', 'price', 'aircraft', 'departure', 'arrival']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    max_display_length = 500

    # def render_column(self, row, column):
    #     # We want to render user as a custom column
    #     if column == 'price':
    #         # escape HTML for security reasons
    #         return escape('{0} {1}'.format(row.customer_firstname, row.customer_lastname))
    #     else:
    #         return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(departure__istartswith=search)
        return qs
    def prepare_results(self, qs):
        json_data = []
        for item in qs:
            id = item.id
            exclude = '' \
                      '<span style="display: flex; flex-flow: row nowrap; justify-content: center;">' \
                      '<a data-tooltip="Informações sobre e-mail" data-position="left center">' \
                      '<i class="ui  info circle icon info-button" style="cursor: pointer;"></i>' \
                      '</a>' \
                      '<a data-tooltip="Excluir e-mail" data-position="left center" >' \
                      '<i class="ui red trash icon delete-button" style="cursor: pointer;"></i>' \
                      '</a></span>'
            json_data.append([
                escape(round(item.distance,2)),
                escape(round(item.price,2)),
                escape(item.aircraft),
                escape(item.departure),
                escape(item.arrival),
            ])
        return json_data

# Create your views here.

def homepage(request):
    return render(request,'homepage.html')
