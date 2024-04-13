from django.shortcuts import render

from django.core.mail import send_mail

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

from .forms import DeviceIssueForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('device_issue_form')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('device_issue_form')  
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def device_issue_form(request):
    if request.method == 'POST':
        form = DeviceIssueForm(request.POST)
        if form.is_valid():
            device_issue = form.save()
            send_email_to_company(device_issue)
            return render(request, 'success.html')
    else:
        form = DeviceIssueForm()
    return render(request, 'device_issue_form.html', {'form': form})

def send_email_to_company(device_issue):
    subject = 'New Device Issue Report'
    message = f'A new device issue report has been submitted:\n\n' \
              f'Name: {device_issue.name}\n' \
              f'Surname: {device_issue.surname}\n' \
              f'Email: {device_issue.email}\n' \
              f'Device Issue: {device_issue.device_issue}\n' \
              f'Serial Number: {device_issue.serial_number}\n' \
              f'Category: {device_issue.category}\n'
    send_mail(subject, message, 'lizapira6@gmail.com', ['lizapira6@gmail.com'])
