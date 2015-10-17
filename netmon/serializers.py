from rest_framework import serializers
from .models import DeviceStatus


class DeviceStatusSerializer(serializers.ModelSerializer):
    device = serializers.StringRelatedField()

    class Meta:
        model = DeviceStatus
        fields = ('id', 'device', 'timestamp')
