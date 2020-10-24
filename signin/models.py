from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    """docstring for profile."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # extra fields
    Class = models.TextField(blank=False)
    
    def __str__(self):
        return self.user.username
class clubs(models.Model):
    """docstring for profile."""
    # extra fields
    clubimage=models.ImageField(upload_to='logos/')
    clubname = models.TextField(blank=False)
    clubtagline=models.TextField(blank=False)
    clubdesc=models.TextField(blank=False)
    memsize=models.TextField(blank=False)
    nofevents=models.TextField(blank=False)
    president=models.TextField(blank=False)
    contact_mail=models.TextField(blank=False)
    def __str__(self):
        return self.clubname
