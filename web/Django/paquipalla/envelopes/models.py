from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 100)

class Envelope(models.Model):
    amount = models.IntegerField()
    motive = models.CharField(max_length = 100)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)
