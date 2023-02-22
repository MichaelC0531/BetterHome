from random import choices
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

WORKS = (
    ('CP','Concrete Pavement'),
    ('WP','Wooden Patio Building/Repairment'),
    ('R', 'House Renovation'),
    ('HM', 'Home Moving'),
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
    date_created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.get_work_display()} with {self.location}"
    
    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'job_id': self.id})
        
    class Meta:
        ordering = ['-date_created']

class Quotation(models.Model):
    price = models.IntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} quot {self.job} for {self.price}"

    class Meta:
        ordering = ['price']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for job_id: {self.job_id} @{self.url}"