from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from model_utils.fields import StatusField
from model_utils import Choices

class StudentGroup(models.Model):
    class Meta:
        ordering = ['name']

    SUBJECTS = Choices(
        'biologi',
        'bioteknologi',
        'kemi',
        'srp',
        'teknikfag',
        'teknologi',
        'andet'
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher')
    name = models.CharField(max_length=100, blank=False)
    students = models.TextField(max_length=1000, blank=False)
    subject = StatusField(choices_name='SUBJECTS')
    grade = models.DecimalField(max_digits=1, decimal_places=0)
    letter = models.CharField(max_length=1, blank=False)
    created = models.DateTimeField(auto_now_add=True)

def is_student_group(user):
    student_group = StudentGroup.objects.filter(user=user).count()
    return student_group != 0
auth.models.User.add_to_class('is_student_group', is_student_group)
