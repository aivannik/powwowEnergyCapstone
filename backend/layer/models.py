from django.db import models

# Create your models here.

class Layer(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    year = models.CharField(max_length=4)
    area = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    