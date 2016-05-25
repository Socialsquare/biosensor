from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from model_utils.fields import StatusField
from model_utils import Choices

class Category(models.Model):
    class Meta:
        ordering = ['name']

    CATEGORY_TYPES = Choices(
        'detector',
        'responder',
        'biobrick'
    )
    name = models.CharField(max_length=100, blank=False)
    category_type = StatusField(choices_name='CATEGORY_TYPES')
