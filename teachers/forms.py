from django import forms
from allauth.account.forms import SignupForm

from .models import School
from studentgroups.models import StudentGroup
from string import ascii_lowercase

class TeacherSignupForm(SignupForm):
    school = forms.ModelChoiceField(label='Gymnasium',
                                   queryset=School.objects.all(),
                                   required=True)
    subjects = forms.fields.CharField(
        label='Emner',
        required=True,
        max_length=400,
        widget=forms.Textarea(attrs={
            'placeholder': 'Emner du underviser i'
            })
    )

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].label = 'Adgangskode'
        self.fields['password1'].widget.attrs['placeholder'] = 'Adgangskode'
        self.fields['password2'].label = 'Gentag adgangskode'
        self.fields['password2'].widget.attrs['placeholder'] = 'Gentag adgangskode'


class StudentGroupForm(forms.Form):
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
            choices=[(v, n.capitalize()) for (n, v) in
                [('', '')] + StudentGroup.SUBJECTS],
            required=True)
    grade = forms.fields.ChoiceField(
            widget=forms.Select, choices=[(i,i) for i in range(1,4)],
            label='Klassetrin',
            required=True)
    letter = forms.fields.ChoiceField(
            widget=forms.Select, choices=[(i,i) for i in list(ascii_lowercase)],
            label='Bogstav',
            required=True)
