from django.db import models
from django.contrib.auth.models import User


class clubs(models.Model):
    """docstring for profile."""
    # extra fields
    clubimage=models.ImageField(upload_to='logos/')
    clubname = models.TextField(blank=False)
    clubtagline=models.TextField(blank=False)
    clubdesc=models.TextField(blank=False)
    clubpurp=models.TextField(blank=False)
    memsize=models.TextField(blank=False)
    nofevents=models.TextField(blank=False)
    clubactivities=models.TextField(blank=False)
    coreteam=models.TextField(blank=False)
    members=models.TextField(blank=True)
    def __str__(self):
        return self.clubname
