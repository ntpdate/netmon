from django.contrib import admin

from .models import User, DeviceType, Device

admin.site.register(User)
admin.site.register(DeviceType)
admin.site.register(Device)
