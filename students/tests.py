from django.contrib.auth.models import User
from django.test import TestCase, Client
from teachers.models import School, Teacher, Invitation
from django.core import mail

import logging
logger = logging.getLogger('biosensor-tests')


class StudentSignupTestCase(TestCase):
    def setUp(self):
        # Create a school
        self.school = School.objects.create(
            name='Test school',
            contact_name='Someone',
            contact_email='someone@somewhere.com',
            password='school-w00t',
            address='Somewhere'
        )
        # With a teacher
        self.teacher_user = User.objects.create_user(
            username='Somewhere Teacher',
            email='teacher@somewhere.com',
            password='w00tw00t'
        )
        self.teacher = Teacher.objects.create(
            user=self.teacher_user,
            school=self.school,
            subjects='Great subjects'
        )
        # And an active invitation
        self.invitation = Invitation.objects.create(
            teacher=self.teacher,
            code='123456'
        )

    def test_students_can_signup(self):
        """Students can sign up using the password and an email is sent"""
        client = Client()

        mails_before = len(mail.outbox)
        response = client.post('/elev/tilmeld/', {
            'code': '123456',
            'email': 'student@somewhere.com',
            'first_name': 'Student',
            'last_name': 'Somename',
            'password1': 'student-password',
            'password2': 'student-password'
        })
        mails_after = len(mail.outbox)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bruger/confirm-email/')
        self.assertEqual(mails_after, mails_before + 1)
