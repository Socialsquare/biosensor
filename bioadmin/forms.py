from django import forms

from teachers.models import School

class SchoolForm(forms.Form):
    name = forms.fields.CharField(max_length=100, required=True)
    contact_name = forms.fields.CharField(max_length=100, required=True)
    contact_email = forms.fields.CharField(max_length=100, required=True)
    address = forms.fields.CharField(
        required=True,
        max_length=400,
        widget=forms.Textarea
    )

