from django import forms

from .models import DeviceIssue

class DeviceIssueForm(forms.ModelForm):
    class Meta:
        model = DeviceIssue
        fields = ['name', 'surname', 'email', 'country', 'device_issue', 'serial_number', 'category']

