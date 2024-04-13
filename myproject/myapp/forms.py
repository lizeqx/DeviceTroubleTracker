from django import forms


class DeviceIssueForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    surname = forms.CharField(max_length=100, label='Surname')
    email = forms.EmailField(label='Email')
    device_issue = forms.CharField(widget=forms.Textarea, label='Device Issue')
    serial_number = forms.CharField(max_length=100, label='Serial Number')
    category = forms.ChoiceField(choices=[('laptop', 'Laptop'), ('phone', 'Phone')], label='Category')