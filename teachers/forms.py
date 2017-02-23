from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
import datetime

from .models import School
from studentgroups.models import StudentGroup
from students.models import Student
from string import ascii_lowercase

import hashlib


class TeacherSignupForm(SignupForm):
    school = forms.ModelChoiceField(
        label='Skole',
        queryset=School.objects.all(),
        empty_label='',
        required=True)
    school_passwd = forms.fields.CharField(
        label='Skolens adgangskode',
        widget=forms.PasswordInput(attrs={'placeholder': 'Skoleadgangskode'}),
        max_length=100,
        required=True)
    subjects = forms.fields.CharField(
        label='Dine fag',
        widget=forms.TextInput(attrs={'placeholder': 'Fag'}),
        required=True,
        max_length=100
    )
    first_name = forms.CharField(
        label='Dit fornavn',
        widget=forms.TextInput(attrs={'placeholder': 'Fornavn'}),
        max_length=30,
        required=True
    )

    last_name = forms.CharField(
        label='Dit efternavn',
        widget=forms.TextInput(attrs={'placeholder': 'Efternavn'}),
        max_length=30,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Din email'
        self.fields['password1'].label = 'Din adgangskode'
        self.fields['password2'].label = 'Gentag din adgangskode'

    def clean(self):
        school_id = self.cleaned_data['school'].id
        school_passwd = self.cleaned_data['school_passwd']

        hashed_passwd = hashlib.sha512(
            school_passwd.encode('utf-8')
        ).hexdigest()

        school = School.objects.filter(id=school_id, password=hashed_passwd)

        if not school:
            raise forms.ValidationError({
                'school_passwd': ["Du har angivet en forkert adgangskode", ]
            })
        return self.cleaned_data


YEAR_CHOICES = [('', '')] + [
    (y, y) for y in range(
        datetime.datetime.now().year - 4, datetime.datetime.now().year + 1
    )
]


class SchoolClassForm(forms.Form):
    letter = forms.fields.CharField(
        label='Bogstav/navn',
        widget=forms.TextInput(),
        required=True,
        max_length=5
    )
    study_field = forms.fields.CharField(
        label='Studieretning',
        widget=forms.TextInput(),
        required=True,
        max_length=20
    )
    enrollment_year = forms.fields.ChoiceField(
        widget=forms.Select, choices=YEAR_CHOICES,
        label='Optagelsesår',
        required=True)


class StudentGroupForm(forms.Form):
    group_id = forms.fields.IntegerField(
        widget=forms.HiddenInput(),
        required=False
    )
    name = forms.fields.CharField(
        label='Gruppenavn',
        max_length=100,
        required=True
    )
    students = forms.ModelMultipleChoiceField(
        label='Elever',
        queryset=None,
        required=False,
        help_text='Vælg gruppens elever (hold ctrl nede for at vælge flere).'
    )

    def __init__(self, *args, **kwargs):
        school_class = kwargs.pop('school_class')
        self.school_class = school_class
        super(StudentGroupForm, self).__init__(*args, **kwargs)
        students_qs = school_class.student_set
        self.fields['students'].queryset = students_qs
        if 'group_id' in self.data:
            student_group_id = self.data['group_id']
        else:
            student_group_id = None
        self.fields['students'].label_from_instance = lambda student: \
            self.get_student_label(student, student_group_id)

    def clean_name(self):
        student_group_id = self.data['group_id']
        student_groups = self.school_class.student_groups

        name = self.cleaned_data['name']  # The suggested name

        similar_student_groups = student_groups.filter(
            name=name
        )
        # If editing a group, we should be able to save it with the same name
        if student_group_id:
            similar_student_groups = similar_student_groups.exclude(
                pk=student_group_id
            )

        if similar_student_groups.exists():
            raise forms.ValidationError(
                'Der eksisterer allerede en gruppe med det navn'
            )
        return name

    @staticmethod
    def get_student_label(student, student_group_id):
        other_student_groups = student.student_groups

        if student_group_id:
            other_student_groups = other_student_groups.exclude(
                pk=student_group_id
            )

        extra = (
            ' (allerede i en anden gruppe)'
            if other_student_groups.exists()
            else ''
        )

        return '%s %s%s' % (
            student.user.first_name,
            student.user.last_name,
            extra
        )
