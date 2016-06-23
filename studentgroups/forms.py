from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

from biobricks.models import Category, Biobrick

class ReportForm(forms.Form):
    resume = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 karakterer',
            required=True)
    method = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 karakterer',
            required=True)
    results = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 karakterer',
            required=True)
    conclusion = forms.fields.CharField(
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 karakterer',
            required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['resume'].label = 'Resumé'
        self.fields['resume'].widget.attrs['placeholder'] = 'Resume'
        self.fields['method'].label = 'Metode'
        self.fields['method'].widget.attrs['placeholder'] = 'Metode'
        self.fields['results'].label = 'Resultater'
        self.fields['results'].widget.attrs['placeholder'] = 'Resultater'
        self.fields['conclusion'].label = 'Diskussion/konklusion'
        self.fields['conclusion'].widget.attrs['placeholder'] = 'Diskussion/konklusion'
