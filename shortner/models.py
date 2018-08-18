from django.db import models

# Create your models here.

class Link(models.Model):
    short = models.CharField(max_length=3)
    original = models.CharField(max_length=300)
    def __str__(self): return self.original[8:30]
    class Meta:
        ordering = ['-pk']