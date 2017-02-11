from django import forms

from teachers.models import Teacher, Invitation
from allauth.account.forms import SignupForm

class StudentSignUpForm(SignupForm):
    code = forms.fields.CharField(
            widget=forms.TextInput(),
            label='Tilmeldingskoden fra din lærer',
            max_length=10,
            required=True)

    first_name = forms.CharField(
        max_length=30,
        label='Dit fornavn',
        required=True)
    last_name = forms.CharField(
        max_length=30,
        label='Dit efternavn',
        required=True)
    school_class = forms.CharField(max_length=10, label='Din klasse')

    def clean(self):
        invitation = Invitation.objects.filter(code=self.cleaned_data['code'])
        if invitation:
            if invitation[0].has_expired():
                raise forms.ValidationError({
                    'code': ["Tilmeldingskoden er udløbet",]
                    })
        else:
            raise forms.ValidationError({
                'code': ["Du har angivet en forkert tilmeldingskode",]
                })

        self.cleaned_data['school'] = invitation[0].teacher.school
        return self.cleaned_data
