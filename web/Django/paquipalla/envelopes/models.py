from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.name

class Envelope(models.Model):
    amount = models.IntegerField()
    motive = models.CharField(max_length = 100)
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __unicode__(self):
        return self.company.name + " " + self.motive
