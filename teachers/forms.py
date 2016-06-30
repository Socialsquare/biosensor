from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User
import datetime

from .models import School
from studentgroups.models import StudentGroup
from string import ascii_lowercase

import hashlib

class TeacherSignupForm(SignupForm):
    school = forms.ModelChoiceField(label='Skole',
            queryset=School.objects.all(),
            empty_label='',
            required=True)
    school_passwd = forms.fields.CharField(
            widget=forms.PasswordInput(),
            label='Skolens adgangskode',
            max_length=100,
            required=True)
    subjects = forms.fields.CharField(
        label='Dine fag',
        required=True,
        max_length=100
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Din email'
        self.fields['password1'].label = 'Din adgangskode'
        self.fields['password2'].label = 'Gentag din adgangskode'

    def clean(self):
        school_id = self.cleaned_data['school'].id
        school_passwd = self.cleaned_data['school_passwd']
        hashed_passwd = hashlib.sha512(school_passwd.encode('utf-8')).hexdigest()
        school = School.objects.filter(id=school_id).filter(password=hashed_passwd)
        if not school:
            raise forms.ValidationError({
                'school_passwd': ["Du har angivet en forkert adgangskode",]
                })
        return self.cleaned_data

YEAR_CHOICES = [('', '')] + [(y, y) for y in range(datetime.datetime.now().year, (datetime.datetime.now().year + 4))]
class StudentGroupForm(forms.Form):
    group_id = forms.fields.IntegerField(
            widget=forms.HiddenInput(),
            required=False)
    name = forms.fields.CharField(
            label='Gruppenavn',
            max_length=100,
            required=True)
    email = forms.fields.CharField(
            label='Kontaktemail',
            max_length=100,
            required=True)
    students = forms.fields.CharField(
            label='Elever',
            max_length=1000,
            required=True,
            widget=forms.Textarea()
            )
    subject = forms.fields.ChoiceField(
            label='Fag',
            widget=forms.Select,
            choices=[(v, n) for (n, v) in
                [('', '')] + StudentGroup.SUBJECTS],
            required=True)
    grade = forms.fields.ChoiceField(
            widget=forms.Select, choices=[('','')]+[(i,i) for i in range(1,4)],
            label='Klasse',
            required=True)
    letter = forms.fields.ChoiceField(
            widget=forms.Select, choices=[(i,i) for i in ['']+list(ascii_lowercase)],
            label='Bogstav',
            required=True)
    year = forms.fields.ChoiceField(
            widget=forms.Select, choices=YEAR_CHOICES,
            label='Afgangsår',
            required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        group_id = self.cleaned_data['group_id']
        if group_id:
            group = StudentGroup.objects.get(id=group_id)
            if email == group.user.email:
                return email

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(u'Der findes allerede en elevgruppe med denne email')
