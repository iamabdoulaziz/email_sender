from django.db import models

class Account (models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Csv (models.Model):
    file = models.FileField(upload_to='csvs/')
    upload_at = models.DateField(auto_now_add=True)
