from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import DeviceStatusSerializer
from .models import User, DeviceType, Device, DeviceStatus
from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        context['status_objects'] = DeviceStatus.objects.all()
        return context


class DeviceStatusList(ListCreateAPIView):
    queryset = DeviceStatus.objects.all()
    serializer_class = DeviceStatusSerializer


class DeviceStatusDetail(RetrieveUpdateDestroyAPIView):
    queryset = DeviceStatus.objects.all()
    serializer_class = DeviceStatusSerializer
