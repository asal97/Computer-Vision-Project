from django.db import models


# Create your models here.

class Taradod(models.Model):
    plate = models.CharField(max_length=30, blank=True)
    color = models.CharField(max_length=10, blank=True)
    type = models.CharField(max_length=20, blank=True)
    seen = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def short_status(self):
        return '%s' % self.plate

    def __str__(self):
        return '%s %s %s %s %s' % (self.plate, self.color, self.type, self.seen, self.approved)
