from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from biobricks.models import Category, Biobrick

class ReportForm(forms.Form):
    resume = forms.fields.CharField(
            label='',
            max_length=10000,
            widget=SummernoteInplaceWidget(),
            help_text='Max 10000 tegn',
            required=True)
    image = forms.fields.FileField(
            label='Billede',
            required=False)
    attachment = forms.fields.FileField(
            label='Fil',
            required=False)

    MAX_UPLOAD_SIZE = 2 * 1024 * 1024

    def clean_image(self):
        content_types = ['png', 'jpeg']
        if 'image' not in self.cleaned_data or not self.cleaned_data['image']:
            return

        image = self.cleaned_data['image']
        content_type = image.name.split('.')[-1]
        if content_type in content_types:
            if image.size > self.MAX_UPLOAD_SIZE:
                raise ValidationError({'image':
                    'Filstørrelsen skal være under %s. Størrelsen på denne fil er %s' %
                    (filesizeformat(self.MAX_UPLOAD_SIZE),
                        filesizeformat(image.size))})
        else:
            raise ValidationError('Du må kun uploade .jpg og .png filer')
        return image

    def clean_attachment(self):
        content_types = ['xls', 'xlsx']
        if 'attachment' not in self.cleaned_data or not self.cleaned_data['attachment']:
            return

        attachment = self.cleaned_data['attachment']
        content_type = attachment.name.split('.')[-1]
        if content_type in content_types:
            if attachment.size > self.MAX_UPLOAD_SIZE:
                raise ValidationError({'attachment':
                    'Filstørrelsen skal være under %s. Størrelsen på denne fil er %s' %
                    (filesizeformat(self.MAX_UPLOAD_SIZE),
                        filesizeformat(attachment.size))})
        else:
            raise ValidationError('Du må kun uploade .xls og .xlsx filer')
        return attachment
