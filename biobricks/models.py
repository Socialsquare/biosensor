from __future__ import unicode_literals

from django.db import models
from django.contrib import auth
from model_utils.fields import StatusField
from model_utils import Choices

TYPES = Choices(
    'detector',
    'responder',
    'entry'
)

class Category(models.Model):
    class Meta:
        ordering = ['name']

    CATEGORY_TYPES = TYPES

    name = models.CharField(max_length=100, blank=False)
    category_type = StatusField(choices_name='CATEGORY_TYPES')

    def __str__(self):
        return self.name

class Biobrick(models.Model):
    BIOBRICK_TYPES = TYPES

    biobrick_type = StatusField(choices_name='BIOBRICK_TYPES')
    category = models.ForeignKey('Category')
    description = models.TextField(max_length=1000, blank=False)
    design = models.TextField(max_length=1000, blank=False)
    igem_part_link = models.TextField(max_length=200, blank=False)
    team_website = models.TextField(max_length=200, blank=False)
    dna_sequence = models.TextField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)
