from django.contrib.auth.models import User
from django.test import TestCase, Client
from teachers.models import School, Teacher
from django.core import mail

import hashlib
import logging
logger = logging.getLogger('biosensor-tests')


class StudentSignupTestCase(TestCase):
    def setUp(self):
        # Create a school
        self.school = School.objects.create(
            name='Test school',
            contact_name='Someone',
            contact_email='someone@somewhere.com',
            password=hashlib.sha512('school-w00t'.encode('utf-8')).hexdigest(),
            address='Somewhere'
        )

    def test_teachers_can_signup(self):
        """Teachers can sign up using the password and an email is sent"""
        client = Client()

        mails_before = len(mail.outbox)
        response = client.post('/laerere/tilmeld', {
            'school': self.school.id,
            'school_passwd': 'school-w00t',
            'email': 'teacher@somewhere.com',
            'first_name': 'Teacher',
            'last_name': 'Somename',
            'password1': 'teacher-password',
            'password2': 'teacher-password',
            'subjects': 'Great subjects!'
        })
        mails_after = len(mail.outbox)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bruger/confirm-email/')
        self.assertEqual(mails_after, mails_before + 1)
