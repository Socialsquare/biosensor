from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse

from studentgroups.models import StudentGroup

def send_student_group_notice(group_name, email, password):
    # TODO: remove this when email is set up on staging
    if django_env == 'staging':
        return

    domain = Site.objects.get(id=settings.SITE_ID).domain
    ctx = {
        'group_name': group_name,
        'email': email,
        'password': password
    }
    subject = 'Velkommen til Biosensor'
    msg = render_to_string('teachers/email/student_group_notice.txt', ctx)
    email_from = settings.DEFAULT_FROM_EMAIL
    email_to = [email]

    msg = EmailMessage(subject, msg, email_from, email_to)
    msg.send()
