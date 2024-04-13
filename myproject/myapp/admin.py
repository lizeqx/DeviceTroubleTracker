from django.contrib import admin
from .models import DeviceIssue

class DeviceIssueAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'country', 'device_issue', 'serial_number', 'category', 'device_image')

admin.site.register(DeviceIssue, DeviceIssueAdmin)
