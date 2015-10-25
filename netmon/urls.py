from django.conf.urls import url
from .views import DeviceStatusDetail, DeviceStatusList, DashboardView

urlpatterns = [
    url(r'^api/deviceStatus/$', DeviceStatusList.as_view(), name='device_status'),
    url(r'^api/deviceStatus/(?P<pk>[0-9]+)/$', DeviceStatusDetail.as_view()),
    url(r'^dashboard/$', DashboardView.as_view()),
]
