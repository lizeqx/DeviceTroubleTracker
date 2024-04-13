from django.db import models

class DeviceIssue(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    device_issue = models.TextField()
    serial_number = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    device_image = models.ImageField(upload_to='device_images/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} {self.surname} - {self.email}'
    
