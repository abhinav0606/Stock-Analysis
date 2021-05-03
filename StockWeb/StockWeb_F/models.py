from django.db import models
class Register(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)

    def __str__(self):
        return self.username
# Create your models here.
