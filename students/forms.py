from django import forms

from teachers.models import Teacher, Invitation
from allauth.account.forms import SignupForm
import logging

logger = logging.getLogger(__name__)


class StudentSignUpForm(SignupForm):
    code = forms.fields.CharField(
            widget=forms.TextInput(),
            label='Tilmeldingskoden fra din lærer',
            max_length=10,
            required=True)

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
