from django.conf.urls import url
from .views import DeviceStatusDetail, DeviceStatusList

urlpatterns = [
    url(r'^deviceStatus/$', DeviceStatusList.as_view()),
    url(r'^deviceStatus/(?P<pk>[0-9]+)/$', DeviceStatusDetail.as_view()),
]
