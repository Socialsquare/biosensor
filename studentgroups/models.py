from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth

class StudentGroup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher')
    email = models.CharField(max_length=100, blank=False)
    names = models.TextField(max_length=1000, blank=False)
    no_students = models.DecimalField(max_digits=1, decimal_places=0)
    subject = models.CharField(max_length=100, blank=False)
    year = models.DecimalField(max_digits=1, decimal_places=0)
    created = models.DateTimeField(auto_now_add=True)

def is_student_group(user):
    student_group = StudentGroup.objects.filter(user=user).count()
    return student_group != 0
auth.models.User.add_to_class('is_student_group', is_student_group)
