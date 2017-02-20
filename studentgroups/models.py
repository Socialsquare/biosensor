from __future__ import unicode_literals

import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.files.storage import default_storage
from model_utils.fields import StatusField
from model_utils import Choices

from biobricks.models import Biosensor

# Student groups


class StudentGroup(models.Model):
    class Meta:
        ordering = ['name']

    name = models.CharField(max_length=100, blank=False)
    school_class = models.ForeignKey('teachers.SchoolClass',
                                     related_name='student_groups')
    students = models.ManyToManyField('students.Student',
                                      related_name='student_groups')
    biosensors = models.ManyToManyField(Biosensor)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'school_class')

    def __str__(self):
        return self.name

    def students_as_list(self):
        return [
            '%s %s' %
            (student.user.first_name, student.user.last_name)
            for student in self.students.all()
        ]


def in_student_group(user):
    student = user.student
    if student:
        return student.student_groups.count() > 0
    else:
        return False


auth.models.User.add_to_class('in_student_group', in_student_group)

# Student reports


def do_upload_image(inst, filename):
    return generate_upload_path(inst, filename, 'images')


def do_upload_attachment(inst, filename):
    return generate_upload_path(inst, filename, 'attachments')


def generate_upload_path(instance, filename, dirname):
    """
    Generate random path name for file.
    @see https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.FileField.upload_to
    """
    ext = os.path.splitext(filename)[1].lstrip('.')
    rand_name = "{}.{}".format(uuid.uuid4().hex, ext)
    if dirname:
        rand_name = "{}/{}".format(dirname, rand_name)
    return rand_name


class StudentReport(models.Model):
    student_group = models.ForeignKey('studentgroups.StudentGroup',
                                      related_name='student_reports')
    biosensor = models.OneToOneField('biobricks.Biosensor',
                                     related_name='student_report')
    resume = models.CharField(
            max_length=4000,
            blank=False)
    method = models.CharField(
            max_length=4000,
            blank=False)
    results = models.CharField(
            max_length=4000,
            blank=False)
    conclusion = models.CharField(
            max_length=4000,
            blank=False)
    image = models.ImageField(
            upload_to=do_upload_image,
            blank=True,
            null=True)
    attachment = models.FileField(
            upload_to=do_upload_attachment,
            blank=True,
            null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}: {}'.format(self.student_group.name, self.biosensor.name)

    def has_existing_image(self):
        return self.image and default_storage.exists(self.image.name)

    def has_existing_attachment(self):
        return self.attachment and default_storage.exists(self.attachment.name)
