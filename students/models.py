from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.ForeignKey('teachers.Schoolclass',
                                     blank=False,
                                     null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s fra %s' % (self.user.email, self.school_class)


def is_student(user):
    teacher = Student.objects.filter(user=user).count()
    return teacher != 0


auth.models.User.add_to_class('is_student', is_student)
