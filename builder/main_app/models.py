from random import choices
from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
WORKS = (
    ('CP','Concrete Pavement'),
    ('WP','Wooden Patio'),
    ('SP','Snow Shovel'),
    ('O','Others')
)
ID = (
    ('SP','Service Provider'),
    ('C','Client')
)
class Identity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identity = models.CharField(
        max_length=50,
        choices=ID
        )

class Job(models.Model):
    work = models.CharField(
        max_length=2,
        choices=WORKS,
        default=WORKS[0][0]
        )
    location = models.CharField(max_length=150)
    description = models.CharField(max_length=5000)
    start_date = models.DateField('Tentative start date')
    duration = models.IntegerField()
    user = models.ManyToManyField(User)

class Quotation(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-price']