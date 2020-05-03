from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    """docstring for profile."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # extra fields
    Class = models.TextField(blank=False)

    def __str__(self):
        return self.user.username
