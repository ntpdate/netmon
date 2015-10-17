from django.contrib import admin

from .models import User, UserAdmin, DeviceType, Device, DeviceAdmin, DeviceStatus, DeviceStatusAdmin

admin.site.register(User, UserAdmin)
admin.site.register(DeviceType)
admin.site.register(Device, DeviceAdmin)
admin.site.register(DeviceStatus, DeviceStatusAdmin)
