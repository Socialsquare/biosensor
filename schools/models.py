from __future__ import unicode_literals

from django.db import models

class School(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100, blank=False)
    contact_name = models.CharField(max_length=100, blank=False)
    contact_email = models.CharField(max_length=100, blank=False)
    address = models.TextField(max_length=400, blank=False)

