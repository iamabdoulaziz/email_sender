from django.db import models

class Account (models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
