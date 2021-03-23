from django.urls import path

from .api import views

app_name = 'route_manager'

urlpatterns = [
    path(route='api/', view=views.IPAddressListCreateAPIView.as_view(), name='ipaddress_rest_api'),
    path(route='api/<path:ip>/',
         view=views.IPAddressRetrieveUpdateDestroyAPIView.as_view(),
         name='ipaddress_detail_rest_api')
]
