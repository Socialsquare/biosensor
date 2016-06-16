from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

from biobricks.models import Category, Biobrick

class ReportForm(forms.Form):
    introduction = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            required=True)
    method = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            required=True)
    results = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            required=True)
    discussion = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            required=True)
    conclusion = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            required=True)
