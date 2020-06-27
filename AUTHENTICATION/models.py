from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    #Photo = models.FileField(upload_to='documents/%Y/%m/%d/', null=True)
    Photo = models.ImageField(upload_to='documents/%Y/%m/%d/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    dob = models.DateField(max_length=20, null=True)
    country = models.CharField(max_length=100, null=True)
    State = models.CharField(max_length=100, null=True)
    District = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=True)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'id': self.id})