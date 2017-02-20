from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
import os

from studentgroups.models import StudentGroup


def send_student_group_notice(student_group):
    for student in student_group.students.all():
        ctx = {
            'student_name': student.user.first_name,
            'group_name': student_group.name
        }
        subject = 'Velkommen til Biosensor'
        msg = render_to_string('teachers/email/student_group_notice.txt', ctx)
        email_from = settings.DEFAULT_FROM_EMAIL
        email_to = [student.user.email]

        msg = EmailMessage(subject, msg, email_from, email_to)
        try:
            msg.send()
        except:
            django_env = os.getenv('DJANGO_ENV', 'development')
            if django_env != 'staging':
                messages.error(request, 'Fejl: kunne ikke afsende velkomst-email til {}'.format(group_name))
