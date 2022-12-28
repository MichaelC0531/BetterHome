from random import choices
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse
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
        choices=ID,
        default=ID[0][0]
        )
    def __str__(self):
        return f"{self.user.username} is a {self.get_identity_display()}"

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_work_display()} with {self.location}"
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cat_id': self.id})

class Quotation(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-price']