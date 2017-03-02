from django import forms

from biobricks.models import Biobrick

class BiosensorForm(forms.Form):
    name = forms.fields.CharField(max_length=100, required=True)
    detector = forms.ModelChoiceField(
        queryset=Biobrick.objects.filter(biobrick_type='detector'),
        empty_label='',
        required=True)
    responder = forms.ModelChoiceField(
        queryset=Biobrick.objects.filter(biobrick_type='responder'),
        empty_label='',
        required=True)
    danger_informed = forms.BooleanField(
        required=True,
        label=(" Min/vores lærer har har givet os information om"
               ", hvordan vi skal håndtere genmodificerede orga"
               "nismer (GMO) i laboratoriet.")
    )
    rapport_pledge = forms.BooleanField(
        required=True,
        label=("Når jeg/vi har lavet en biosensor i laboratoriet vil vi lægge"
               " et billede og et kort resumé op, som beskriver biosensoren.")
    )

    def __init__(self, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Navn'
        self.fields['detector'].label = 'Detektor gen'
        self.fields['responder'].label = 'Respons gen'

# We don't need them to check stuff again, when editing.
class BiosensorEditForm(BiosensorForm):
    def __init__(self, *args, **kwargs):
        super(BiosensorForm, self).__init__(*args, **kwargs)
        self.fields.pop('danger_informed')
        self.fields.pop('rapport_pledge')
