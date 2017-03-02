import string
from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from biobricks.models import Category, Biobrick

class SchoolForm(forms.Form):
    name = forms.fields.CharField(
            label='Navn',
            max_length=100,
            required=True)
    contact_name = forms.fields.CharField(
            label='Kontaktperson navn',
            max_length=100,
            required=True)
    contact_email = forms.fields.CharField(
            label='Kontaktperson email',
            max_length=100,
            required=True)
    address = forms.fields.CharField(
            label='Adresse',
            required=True,
            max_length=400,
            widget=forms.Textarea
    )

class CategoryForm(forms.Form):
    name = forms.fields.CharField(
            label='Navn',
            max_length=100,
            required=True)
    category_type = forms.fields.ChoiceField(
            label='Kategori type',
            widget=forms.Select,
            choices=[(v, n.capitalize()) for (n, v) in
                [('', '')] + Category.CATEGORY_TYPES],
            required=True)

class BiobrickForm(forms.Form):
    name = forms.fields.CharField(
            label='Navn',
            max_length=100,
            required=True)
    category = forms.ModelChoiceField(
            label='Kategori',
            queryset=Category.objects.all(),
            empty_label='',
            required=True)
    description = forms.fields.CharField(
            label='Beskrivelse',
            max_length=10000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 10000 tegn',
            required=True)
    design = forms.fields.CharField(
            label='Design',
            max_length=10000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 10000 tegn',
            required=True)
    igem_part = forms.fields.CharField(
            label='iGEM part',
            max_length=200,
            required=True)
    team_website = forms.fields.CharField(
            label='iGEM Team Wiki',
            max_length=200,
            required=True)
    dna_sequence = forms.fields.CharField(
            label='DNA sekvens',
            max_length=200,
            required=True)
    coord_x = forms.fields.ChoiceField(
            label='MTP x-koordinat',
            widget=forms.Select,
            choices=[('', '-'*9)]+[(i, i) for i in range(1,13)],
            required=True)
    coord_y = forms.fields.ChoiceField(
            label='MTP y-koordinat',
            widget=forms.Select,
            choices=[('', '-'*9)]+[(l, l.upper()) for l in string.ascii_lowercase][:8],
            required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['team_website'].widget.attrs['value'] = 'http://'

    def filter_categories(self, biobrick_type):
        categories = self.fields['category'].queryset.filter(category_type=biobrick_type)
        self.fields['category'].queryset = categories

class BiosensorForm(forms.Form):
    name = forms.fields.CharField(
            label='Navn',
            max_length=100,
            required=True)
    detector = forms.ModelChoiceField(
            label='Detektor gen',
            queryset=Biobrick.objects.filter(biobrick_type='detector'),
            empty_label='',
            required=True)
    responder = forms.ModelChoiceField(
            label='Respons gen',
            queryset=Biobrick.objects.filter(biobrick_type='responder'),
            empty_label='',
            required=True)
    category = forms.ModelChoiceField(
            label='Kategori',
            queryset=Category.objects.filter(category_type='biosensor'),
            empty_label='',
            required=True)
    problem_description = forms.fields.CharField(
            label='Problemformulering',
            max_length=1000,
            widget=forms.Textarea,
            required=True)
    risk_description = forms.fields.CharField(
            label='Risikobeskrivelse',
            max_length=1000,
            widget=forms.Textarea,
            required=True)
