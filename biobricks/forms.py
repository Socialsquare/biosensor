from django import forms

from biobricks.models import Category, Biobrick

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
            help_text='Hvorfor er biosensoren vigtig? Hvilket problem løser den?',
            required=True)
    risk_description = forms.fields.CharField(
            max_length=1000,
            widget=forms.Textarea,
            help_text='Er der nogen risiko forbundet med biosensoren? Er der '\
                    + 'noget som man skal være forsigtig med når '\
                    + 'eksperimentet udføres?',
            required=True)

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Navn'
        self.fields['name'].widget.attrs['placeholder'] = 'Navn'
        self.fields['detector'].label = 'Detektor gen'
        self.fields['responder'].label = 'Respons gen'
        self.fields['category'].label = 'Kategori'
        self.fields['category'].widget.attrs['placeholder'] = 'Kategori'
        self.fields['problem_description'].label = 'Problembeskrivelse'
        self.fields['problem_description'].widget.attrs['placeholder'] = 'Problembeskrivelse'
        self.fields['risk_description'].label = 'Risikobeskrivelse'
        self.fields['risk_description'].widget.attrs['placeholder'] = 'Risikobeskrivelse'
