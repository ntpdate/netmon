from rest_framework import serializers
from .models import DeviceStatus


class DeviceStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceStatus
        fields = ('id', 'device', 'timestamp')
