from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DeviceStatusSerializer
from .models import DeviceStatus


class DeviceStatusList(ListCreateAPIView):
    queryset = DeviceStatus.objects.all()
    serializer_class = DeviceStatusSerializer


class DeviceStatusDetail(RetrieveUpdateDestroyAPIView):
    queryset = DeviceStatus.objects.all()
    serializer_class = DeviceStatusSerializer
