from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Column(models.Model):
    title = models.CharField(max_length=100)
    position = models.IntegerField()

class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    position = models.IntegerField()
    column = models.ForeignKey(Column, related_name='cards', on_delete=models.CASCADE)
