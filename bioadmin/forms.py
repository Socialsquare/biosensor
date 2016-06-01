from django import forms
from biobricks.models import Category

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
    category_type = forms.fields.ChoiceField(
            widget=forms.Select,
            choices=[(v, n.capitalize()) for (n, v) in
                [('', '')] + Category.CATEGORY_TYPES],
            required=True)
    name = forms.fields.CharField(max_length=100, required=True)

class BiobrickForm(forms.Form):
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
    igem_part_link = forms.fields.CharField(max_length=200, required=True)
    team_website = forms.fields.CharField(max_length=200, required=True)
    dna_sequence = forms.fields.CharField(max_length=200, required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['igem_part_link'].widget.attrs['value'] = 'http://'
        self.fields['team_website'].widget.attrs['value'] = 'http://'
        self.fields['dna_sequence'].widget.attrs['placeholder'] = 'DNA sequence'

    def filter_categories(self, biobrick_type):
        categories = self.fields['category'].queryset.filter(category_type=biobrick_type)
        self.fields['category'].queryset = categories
