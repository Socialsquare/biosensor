from django import forms
from allauth.account.forms import SignupForm

from .models import School

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


class NewStudentGroupForm(SignupForm):
    names = forms.fields.CharField(
            label='Navne',
            max_length=1000,
            required=True,
            widget=forms.Textarea()
            )
    no_students = forms.fields.IntegerField(label='Antal studerende', min_value=1, max_value=9, required=True)
    subject = forms.fields.CharField(label='Fag', max_length=100, required=True)
    year = forms.fields.IntegerField(label='Årgang', min_value=1, max_value=3, required=True)
