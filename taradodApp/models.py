from django.db import models


# Create your models here.

class Taradod(models.Model):
    plate = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=20, blank=True)
    seen = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
