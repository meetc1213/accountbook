from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    """docstring for profile."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # extra fields
    Class = models.TextField(blank=False)

    def __str__(self):
        return self.user.username

class entries(models.Model):
    """docstring for profile."""
    # extra fields
    clientname = models.TextField(blank=False)
    date=models.TextField(blank=False)
    amount=models.TextField(blank=False)
    source_name=models.TextField(blank=False)
    source_descip=models.TextField(blank=False)
    cred_deb=models.TextField(blank=False)
    def __str__(self):
        return (self.clientname+" "+self.date)
