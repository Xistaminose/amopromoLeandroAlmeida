from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'flights', views.flightViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='flight_rest')),
    url(r'^my/datatable/data/$', views.OrderListJson.as_view(), name='order_list_json'),
    path('test/',views.homepage)
]