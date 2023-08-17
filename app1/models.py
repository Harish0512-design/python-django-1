from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField()
    salary = models.FloatField()
    phone_number = models.IntegerField()
    pincode = models.IntegerField(default=None)
