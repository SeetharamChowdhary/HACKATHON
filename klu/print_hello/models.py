from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=122)
    password=models.EmailField(max_length=122)
    email=models.CharField(max_length=12)
    firstname = models.CharField(max_length=30)

class login(models.Model):
    user=models.CharField(max_length=122)
    password=models.CharField(max_length=122)

    owner = models.ForeignKey("Register", on_delete=models.SET_NULL, null=True)