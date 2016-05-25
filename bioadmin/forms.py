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
    name = forms.fields.CharField(max_length=100, required=True)
    category_type = forms.fields.ChoiceField(
            widget=forms.Select,
            choices=[(v, n.capitalize()) for (n, v) in
                [('', '')] + Category.CATEGORY_TYPES],
            required=True)
