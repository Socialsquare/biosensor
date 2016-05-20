from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100, blank=False)
    contact_name = models.CharField(max_length=100, blank=False)
    contact_email = models.CharField(max_length=100, blank=False)
    address = models.TextField(max_length=400, blank=False)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('School')
    subjects = models.TextField(max_length=400, blank=False)
    created = models.DateTimeField(auto_now_add=True)
