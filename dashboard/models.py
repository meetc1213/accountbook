from django.db import models
from django.contrib.auth.models import User


class clubs(models.Model):
    """docstring for profile."""
    # extra fields
    clubname = models.TextField(blank=False)

    def __str__(self):
        return self.clubname
