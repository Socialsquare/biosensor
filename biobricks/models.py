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
        'biosensor'
    )

    name = models.CharField(max_length=100, blank=False)
    category_type = StatusField(choices_name='CATEGORY_TYPES')

    def __str__(self):
        return self.name

    def is_empty(self):
        model = self.category_type == 'biosensor' and Biosensor or Biobrick
        return not bool(model.objects.filter(category_id=self.id))

class Biobrick(models.Model):
    BIOBRICK_TYPES = Choices(
        'detector',
        'responder',
    )

    biobrick_type = StatusField(choices_name='BIOBRICK_TYPES')
    category = models.ForeignKey('Category')
    name = models.TextField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    design = models.TextField(max_length=1000, blank=False)
    igem_part = models.TextField(max_length=20, blank=False)
    team_website = models.TextField(max_length=200, blank=False)
    dna_sequence = models.TextField(max_length=200, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Biosensor(models.Model):
    user = models.ForeignKey('auth.User')
    detector = models.ForeignKey('Biobrick', related_name='detectors')
    responder = models.ForeignKey('Biobrick', related_name='responders')
    category = models.ForeignKey('Category')
    name = models.TextField(max_length=100, blank=False)
    problem_description = models.TextField(max_length=1000, blank=False)
    risk_description = models.TextField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
