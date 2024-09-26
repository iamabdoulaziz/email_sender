from django.db import models
from datetime import datetime, timedelta

class Account (models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Csv (models.Model):
    file = models.FileField(upload_to='csvs/')
    upload_at = models.DateField(auto_now_add=True)

class OTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

def is_valid(self):
    return datetime.now() < self.created_at + timedelta(minutes=5)
