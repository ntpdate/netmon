from django.contrib import admin

from .models import User, UserAdmin, DeviceType, Device, DeviceAdmin

admin.site.register(User, UserAdmin)
admin.site.register(DeviceType)
admin.site.register(Device, DeviceAdmin)
