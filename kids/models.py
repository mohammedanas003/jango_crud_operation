from django.db import models

# Create your models here.

class Employee(models.Model):
    Name=models.CharField(max_length=100)
    Role=models.CharField(max_length=100)
    Experience=models.IntegerField()
    Salary=models.IntegerField()

