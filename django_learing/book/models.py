from django.db import models

# Create your models here.
class UserInfo(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=128)