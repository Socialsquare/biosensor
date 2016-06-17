from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

from biobricks.models import Category, Biobrick

class ReportForm(forms.Form):
    introduction = forms.fields.CharField(
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
    discussion = forms.fields.CharField(
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
        self.fields['introduction'].label = 'Introduktion'
        self.fields['introduction'].widget.attrs['placeholder'] = 'Introduktion'
        self.fields['method'].label = 'Metode'
        self.fields['method'].widget.attrs['placeholder'] = 'Metode'
        self.fields['results'].label = 'Resultater'
        self.fields['results'].widget.attrs['placeholder'] = 'Resultater'
        self.fields['discussion'].label = 'Diskussion'
        self.fields['discussion'].widget.attrs['placeholder'] = 'Diskussion'
        self.fields['conclusion'].label = 'Konklusion'
        self.fields['conclusion'].widget.attrs['placeholder'] = 'Konklusion'
