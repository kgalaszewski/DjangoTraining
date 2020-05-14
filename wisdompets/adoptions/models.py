from django.db import models


class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]

    name = models.CharField(max_length=100, blank=True)
    submitter = models.CharField(max_length=30, blank=True)
    species = models.CharField(max_length=30, blank=True)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    # do modelu pojdzie tylko M lub F, dla uzytkowanika bedzie male lub female, stad len 1
    sex = models.CharField(choices=SEX_CHOICES, max_length=1)
    submission_date = models.DateTimeField()
    # blank i null to prawie to samo ale dla Int blank to 0 czyli false wiec trzeba dac nullable
    age = models.IntegerField(null=True)
    # many to many relationship
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
