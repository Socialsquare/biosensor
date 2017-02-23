from django.contrib.auth.models import User
from django.test import TestCase, Client
from teachers.models import School, Teacher, SchoolClass, SchoolClassCode
from students.forms import StudentSignUpForm
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
        # A school class
        self.school_class = SchoolClass.objects.create(
            school=self.school,
            enrollment_year=2017,
            letter='x',
            study_field='Testing'
        )
        # And an active school class code
        self.school_class_code = SchoolClassCode.create(
            school_class=self.school_class
        )
        # And some info about our student
        self.student_info = {
            'code': self.school_class_code.code,
            'email': 'student@somewhere.com',
            'first_name': 'Student',
            'last_name': 'Somename',
            'password1': 'student-password',
            'password2': 'student-password'
        }

    def test_students_can_signup(self):
        """Students can sign up using the password and an email is sent"""
        client = Client()

        mails_before = len(mail.outbox)

        response = client.post('/elev/tilmeld/', self.student_info)
        mails_after = len(mail.outbox)

        student = User.objects.get(email=self.student_info['email'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bruger/confirm-email/')

        self.assertTrue(student)
        self.assertEqual(student.first_name, self.student_info['first_name'])

        self.assertEqual(mails_after, mails_before + 1)

    def test_attributes_are_required(self):
        """Not inputing required attributes results in failure"""
        invalid_info = self.student_info
        invalid_info['first_name'] = ''
        form = StudentSignUpForm(invalid_info)

        self.assertFalse(form.is_valid())
