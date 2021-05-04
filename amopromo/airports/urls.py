from django.urls import include, path
from rest_framework import routers
from . import views
from flights.views import flightViewSet

router = routers.DefaultRouter()
router.register(r'airports', views.airportViewSet)
router.register(r'flights', flightViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='airports_rest'))
]