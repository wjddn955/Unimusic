from django.db import models


# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length=30, null=False)
    desc = models.CharField(max_length=400, null=False)
    song1 = models.CharField(max_length=50, null=False)
    song2 = models.CharField(max_length=50, null=False)
    song3 = models.CharField(max_length=50, null=False)


class Audio(models.Model):
    names = models.CharField(max_length=500, null=True,default=False)
    file = models.FileField(upload_to='audio')
