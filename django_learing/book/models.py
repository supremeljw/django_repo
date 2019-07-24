from django.db import models

# Create your models here.
class UserInfo(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=128)
    def __str__(self):
        return self.email
    def __repr__(self):
        return self.email