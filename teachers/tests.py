from django.contrib.auth.models import User
from django.test import TestCase, Client
from teachers.models import School, Teacher, SchoolClass, SchoolClassCode
from django.core import mail
from django.db.utils import IntegrityError

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

        teacher_info = {
            'school': self.school.id,
            'school_passwd': 'school-w00t',
            'email': 'teacher@somewhere.com',
            'first_name': 'Teacher',
            'last_name': 'Somename',
            'password1': 'teacher-password',
            'password2': 'teacher-password',
            'subjects': 'Great subjects!'
        }

        response = client.post('/laerere/tilmeld', teacher_info)
        mails_after = len(mail.outbox)

        teacher = User.objects.get(email=teacher_info['email'])

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/bruger/confirm-email/')

        self.assertTrue(teacher)
        self.assertEqual(teacher.first_name, teacher_info['first_name'])

        self.assertEqual(mails_after, mails_before + 1)

    def test_school_class_code_unique(self):
        """School class codes are unique"""
        # Change the length of codes to a single number, i.e. 10 possibilities.
        SchoolClassCode.CODE_LENGTH = 1
        # Can we generate 10 different codes?
        codes_generated = list()
        for c in range(10):
            # Create a school class
            school_class = SchoolClass.objects.create(
                school=self.school,
                enrollment_year=2017,
                letter='Code School #%d' % c,
                study_field='Testing'
            )
            school_class_code = SchoolClassCode.create(school_class)
            self.assertNotIn(school_class_code.code, codes_generated)
            codes_generated.append(school_class_code.code)
        self.assertEqual(len(codes_generated), 10)
        SchoolClassCode.CODE_LENGTH = 6

        # Check that we cannot create two codes that are equal - even if we try
        # Creating two school classes
        school_class_a = SchoolClass.objects.create(
            school=self.school,
            enrollment_year=2017,
            letter='Code School A',
            study_field='Testing'
        )
        school_class_b = SchoolClass.objects.create(
            school=self.school,
            enrollment_year=2017,
            letter='Code School A',
            study_field='Testing'
        )
        # And the creating two school class codes
        school_class_code_a = SchoolClassCode.create(school_class_a)
        school_class_code_b = SchoolClassCode.create(school_class_b)
        # Try overwriting the b code with a
        msg = 'UNIQUE constraint failed: teachers_schoolclasscode.code'
        with self.assertRaisesMessage(IntegrityError, msg):
            school_class_code_b.code = school_class_code_a.code
            school_class_code_b.save()
