from django.db import models


# Create your models here.

class Taradod(models.Model):
    plate = models.CharField(max_length=50, blank=True)
    img = models.ImageField(upload_to='TaradodPic/', blank=True)
    seen = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def short_status(self):
        return '%s' % self.plate

    def __str__(self):
        return '%s %s %s' % (self.plate, self.seen, self.approved)
