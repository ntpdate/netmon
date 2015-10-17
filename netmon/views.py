from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DeviceStatusSerializer
from .models import DeviceStatus


class DeviceStatusList(ListCreateAPIView):
    """
    Return a list of all the tasks, or
    create new ones
    """
    queryset = DeviceStatus.objects.all()
    serializer_class = DeviceStatusSerializer


class DeviceStatusDetail(RetrieveUpdateDestroyAPIView):
    """
    Return a specific task, update it, or delete it.
    """
    queryset = DeviceStatus.objects.all()
    serializer_class = DeviceStatusSerializer
