from django import forms

from teachers.models import Teacher, SchoolClassCode
from allauth.account.forms import SignupForm


class StudentSignUpForm(SignupForm):
    code = forms.fields.CharField(
        label='Indtast klassekoden',
        widget=forms.TextInput(attrs={'placeholder': 'Klassekode'}),
        max_length=10,
        required=True
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
        school_class_code = SchoolClassCode.objects.filter(
            code=self.cleaned_data['code']
        )
        if school_class_code:
            if school_class_code[0].has_expired():
                raise forms.ValidationError({
                    'code': ["Tilmeldingskoden er udløbet"]
                })
        else:
            raise forms.ValidationError({
                'code': ["Du har angivet en forkert tilmeldingskode"]
            })

        self.cleaned_data['school_class'] = school_class_code[0].school_class
        return self.cleaned_data
