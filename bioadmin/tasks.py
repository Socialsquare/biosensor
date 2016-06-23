from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
import os

from studentgroups.models import StudentGroup

def send_school_notice(school, password):
    # TODO: remove this when email is set up on staging
    django_env = os.getenv('DJANGO_ENV', 'development')
    if django_env == 'staging':
        return

    domain = Site.objects.get(id=settings.SITE_ID).domain
    ctx = {
        'school': school,
        'password': password,
        'signup_link':'http://{}'.format(domain) + reverse('teachers:signup')
    }
    subject = 'Velkommen til Biosensor'
    txt_msg = render_to_string('bioadmin/email/school_notice.txt', ctx)
    email_from = settings.DEFAULT_FROM_EMAIL
    email_to = [school.contact_email, ]

    msg = EmailMessage(subject, txt_msg, email_from, email_to)
    msg.send()

