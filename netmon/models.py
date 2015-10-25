from django.db import models
from django.contrib import admin


class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


class DeviceType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Device(models.Model):
    mac_address = models.CharField(max_length=17, primary_key=True)
    device_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, blank=True)
    device_type = models.ForeignKey(DeviceType, null=True, blank=True)

    def __str__(self):
        return self.mac_address

    def __unicode__(self):
        return self.mac_address


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('mac_address', 'device_name', 'get_username', 'get_device_type')

    @classmethod
    def get_username(cls, device):
        if device.user:
            return device.user.username
        else:
            return '<N/A>'

    @classmethod
    def get_device_type(cls, device):
        if device.device_type:
            return device.device_type.name
        else:
            return '<N/A>'


class DeviceStatus(models.Model):
    device = models.ForeignKey(Device)
    timestamp = models.DateTimeField()


class DeviceStatusAdmin(admin.ModelAdmin):
    list_display = ('device', 'timestamp')
