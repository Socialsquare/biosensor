from __future__ import unicode_literals

from datetime import timedelta, datetime
import random
import string

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from django.utils.crypto import get_random_string
import hashlib


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

    # Generates a random password, hashes it and returns the original
    # so we can send it by mail.
    def set_random_password(self):
        password = self.generate_random_password()
        self.password = self.hash_password(password)
        return password

    @staticmethod
    def generate_random_password():
        return get_random_string()

    @staticmethod
    def hash_password(password):
        return hashlib.sha512(password.encode('utf-8')).hexdigest()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.ForeignKey('School')
    subjects = models.TextField(max_length=400, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user.first_name:
            name = '%s %s' % (self.user.first_name, self.user.last_name)
        else:
            name = self.user.email
        return '%s fra %s' % (
            name,
            self.school
        )


def is_teacher(user):
    teacher = Teacher.objects.filter(user=user).count()
    return teacher != 0


auth.models.User.add_to_class('is_teacher', is_teacher)


class SchoolClass(models.Model):
    school = models.ForeignKey('School')
    enrollment_year = models.PositiveIntegerField(blank=False)
    letter = models.CharField(blank=False, max_length=10)
    study_field = models.CharField(blank=False, max_length=20)

    def __str__(self):
        return '%s %s-klasse årgang %d fra %s' % (
            self.study_field,
            self.letter,
            self.enrollment_year,
            self.school
        )


class ActiveSchoolClassCodeManager(models.Manager):
    def get_queryset(self):
        queryset = super(ActiveSchoolClassCodeManager, self).get_queryset()
        now = timezone.now()
        created_before = now - SchoolClassCode.EXPIRATION_DELTA
        return queryset.filter(created__gt=created_before)


class SchoolClassCode(models.Model):
    EXPIRATION_DELTA = timedelta(days=7)
    CODE_LENGTH = 6

    school_class = models.OneToOneField(SchoolClass,
                                        on_delete=models.CASCADE,
                                        null=True,
                                        related_name='school_class_code')
    code = models.TextField(max_length=10, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    active_objects = ActiveSchoolClassCodeManager()

    def get_expiry(self):
        return self.created + self.EXPIRATION_DELTA

    def has_expired(self):
        return timezone.now() > self.get_expiry()

    def generate_code():
        LENGTH = SchoolClassCode.CODE_LENGTH
        while True:
            code = ''.join(random.choice(string.digits) for _ in range(LENGTH))
            # Check that this is actually unique
            if not SchoolClassCode.objects.filter(code=code).exists():
                return code

    def create(school_class):
        code = SchoolClassCode.generate_code()
        return SchoolClassCode.objects.create(school_class=school_class,
                                              code=code)

    def __str__(self):
        expired_maybe = ' (udløbet)' if self.has_expired() else ''
        return 'Klassekode %s%s' % (self.code, expired_maybe)
