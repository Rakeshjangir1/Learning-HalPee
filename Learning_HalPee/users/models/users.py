from django.db import models


class user_registration(models.Model):
    updated_on = models.DateTimeField(auto_now=True, null=True)
    Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50, null=True)
    Phone_number = models.IntegerField()
    Email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

