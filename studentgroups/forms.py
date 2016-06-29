from django import forms
from django_summernote.widgets import SummernoteInplaceWidget

from biobricks.models import Category, Biobrick

class ReportForm(forms.Form):
    resume = forms.fields.CharField(
            label='Resumé',
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 tegn',
            required=True)
    method = forms.fields.CharField(
            label='Metode',
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 tegn',
            required=True)
    results = forms.fields.CharField(
            label='Resultater',
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 tegn',
            required=True)
    conclusion = forms.fields.CharField(
            label='Diskussion og konklusion',
            max_length=4000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 4000 tegn',
            required=True)
    image = forms.fields.FileField(
            label='Billede',
            required=False)
    image = forms.fields.ImageField(
            label='Billede',
            required=False)

    CONTENT_TYPES = [
        'png', 'jpeg', ''
    ]
    MAX_UPLOAD_SIZE = 2 * 1024 * 1024

    def clean_image(self):
        if 'image' not in self.cleaned_data or\
                not self.cleaned_data['image']:
            return
        image = self.cleaned_data['image']
        content_type = image.content_type.split('/')[1]
        if content_type in self.CONTENT_TYPES:
            if image.size > self.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(
                    _('Please keep filesize under %s. Current filesize %s') %
                    (filesizeformat(self.MAX_UPLOAD_SIZE),
                     filesizeformat(image.size)))
        else:
            raise forms.ValidationError(_('File type is not allowed'))
        return image

