from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)


class DeviceType(models.Model):
    name = models.CharField(max_length=100)


class Device(models.Model):
    mac_address = models.CharField(max_length=17)
    device_name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    device_type = models.ForeignKey(DeviceType)
