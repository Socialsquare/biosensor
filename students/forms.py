from django import forms

from allauth.account.forms import SignupForm

class StudentSignUpForm(SignupForm):
    code = forms.fields.CharField(
            widget=forms.PasswordInput(),
            label='Adgangskoden fra din lærer',
            max_length=10,
            required=True)
