
from django.db import models

from django.contrib.auth.models import User



class Symptom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.


class d_dis(models.Model):
    name=models.CharField(max_length=100)
    dis = models.TextField()

    def __str__(self):
        return self.name     


# Create your models here.
