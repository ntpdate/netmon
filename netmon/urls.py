from django.conf.urls import url
from .views import DeviceStatusDetail, DeviceStatusList, DashboardView

urlpatterns = [
    url(r'^api/deviceStatus/$', DeviceStatusList.as_view(), name='api_device_status_list'),
    url(r'^api/deviceStatus/(?P<pk>[0-9]+)/$', DeviceStatusDetail.as_view(), name='api_device_status_detail'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
]
