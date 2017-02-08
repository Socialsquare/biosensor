from __future__ import unicode_literals

from datetime import timedelta, datetime
import random
import string

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone


class School(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100, blank=False)
    contact_name = models.CharField(max_length=100, blank=False)
    contact_email = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=400, blank=False)
    address = models.TextField(max_length=400, blank=False)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('School')
    subjects = models.TextField(max_length=400, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s fra %s' % (self.user.email, self.school)


def is_teacher(user):
    teacher = Teacher.objects.filter(user=user).count()
    return teacher != 0


auth.models.User.add_to_class('is_teacher', is_teacher)


class ActiveInvitationManager(models.Manager):
    def get_queryset(self):
        queryset = super(ActiveInvitationManager, self).get_queryset()
        now = timezone.now()
        created_before = now - Invitation.EXPIRATION_DELTA
        return queryset.filter(created__gt=created_before)


class Invitation(models.Model):
    EXPIRATION_DELTA = timedelta(days=7)
    CODE_LENGTH = 6

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    code = models.TextField(max_length=10, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    active_objects = ActiveInvitationManager()

    def get_expiry(self):
        return self.created + self.EXPIRATION_DELTA

    def has_expired(self):
        return timezone.now() > self.get_expiry()

    def generate_code():
        LENGTH = Invitation.CODE_LENGTH
        return ''.join(random.choice(string.digits) for _ in range(LENGTH))

    def create(teacher):
        code = Invitation.generate_code()
        return Invitation.objects.create(teacher=teacher, code=code)

    def __str__(self):
        expired_maybe = ' (udløbet)' if self.has_expired() else ''
        return 'Invitationskode %s%s' % (self.code, expired_maybe)
