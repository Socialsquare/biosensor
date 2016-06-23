import string
from django import forms
from biobricks.models import Category, Biobrick

class SchoolForm(forms.Form):
    name = forms.fields.CharField(max_length=100, required=True)
    contact_name = forms.fields.CharField(max_length=100, required=True)
    contact_email = forms.fields.CharField(max_length=100, required=True)
    address = forms.fields.CharField(
        required=True,
        max_length=400,
        widget=forms.Textarea
    )

class CategoryForm(forms.Form):
    name = forms.fields.CharField(max_length=100, required=True)
    category_type = forms.fields.ChoiceField(
            widget=forms.Select,
            choices=[(v, n.capitalize()) for (n, v) in
                [('', '')] + Category.CATEGORY_TYPES],
            required=True)

class BiobrickForm(forms.Form):
    name = forms.fields.CharField(max_length=100, required=True)
    category = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            required=True)
    description = forms.fields.CharField(
            max_length=1000,
            widget=forms.Textarea,
            required=True)
    design = forms.fields.CharField(
            max_length=1000,
            widget=forms.Textarea,
            required=True)
    igem_part = forms.fields.CharField(max_length=200, required=True)
    team_website = forms.fields.CharField(max_length=200, required=True)
    dna_sequence = forms.fields.CharField(max_length=200, required=True)
    coord_x = forms.fields.ChoiceField(
            widget=forms.Select,
            choices=[('', '-'*9)]+[(i, i) for i in range(1,13)],
            required=True)
    coord_y = forms.fields.ChoiceField(
            widget=forms.Select,
            choices=[('', '-'*9)]+[(l, l.upper()) for l in string.ascii_lowercase][:8],
            required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['team_website'].widget.attrs['value'] = 'http://'
        self.fields['dna_sequence'].widget.attrs['placeholder'] = 'DNA sequence'

    def filter_categories(self, biobrick_type):
        categories = self.fields['category'].queryset.filter(category_type=biobrick_type)
        self.fields['category'].queryset = categories

class BiosensorForm(forms.Form):
    name = forms.fields.CharField(max_length=100, required=True)
    detector = forms.ModelChoiceField(
            queryset=Biobrick.objects.filter(biobrick_type='detector'),
            required=True)
    responder = forms.ModelChoiceField(
            queryset=Biobrick.objects.filter(biobrick_type='responder'),
            required=True)
    category = forms.ModelChoiceField(
            queryset=Category.objects.filter(category_type='biosensor'),
            required=True)
    problem_description = forms.fields.CharField(
            max_length=1000,
            widget=forms.Textarea,
            required=True)
    risk_description = forms.fields.CharField(
            max_length=1000,
            widget=forms.Textarea,
            required=True)
