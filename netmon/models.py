from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class DeviceType(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Device(models.Model):
    mac_address = models.CharField(max_length=17, unique=True)
    device_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    device_type = models.ForeignKey(DeviceType)


class DeviceStatus(models.Model):
    device = models.ForeignKey(Device)
    timestamp = models.DateTimeField()
