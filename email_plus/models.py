from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from datetime import timedelta
from django.utils import timezone


class Account(AbstractBaseUser, models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Csv (models.Model):
    file = models.FileField(upload_to='csvs/')
    upload_at = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

class OTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def is_valid(self):
        created_at = self.created_at
        return timezone.now() < created_at + timedelta(minutes=5)
