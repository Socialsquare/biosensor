from django import forms
from django_summernote.widgets import SummernoteInplaceWidget
from django.core.exceptions import ValidationError

from biobricks.models import Category, Biobrick

MAX_UPLOAD_SIZE = 2 * 1024 * 1024


def clean_file(the_file, content_types):
    if the_file:
        if the_file.content_type in content_types:
            if the_file.size > MAX_UPLOAD_SIZE:
                raise ValidationError({
                    'image': 'Størrelsen skal være under %s, filen er %s' % (
                        filesizeformat(self.MAX_UPLOAD_SIZE),
                        filesizeformat(the_file.size)
                    )
                })
        else:
            raise ValidationError('Du må kun uploade filer af typerne %s' % (
                ' / '.join(content_types.values())
            ))
    return the_file


class ResumeForm(forms.Form):
    resume = forms.fields.CharField(
        label='',
        max_length=10000,
        widget=SummernoteInplaceWidget(),
        help_text='Max 10000 tegn',
        required=True
    )


class PhotoForm(forms.Form):
    image = forms.fields.ImageField(
        label='',
        required=True
    )

    def clean_image(self):
        the_file = self.cleaned_data.get('image', None)
        content_types = {
            'image/png': '.png',
            'image/jpeg': '.jpeg',
            'image/gif': '.gif'
        }
        return clean_file(the_file, content_types)


class ReportForm(forms.Form):
    attachment = forms.fields.FileField(
        label='',
        help_text='Gem rapporten som en .pdf og upload den her',
        required=True
    )

    def clean_attachment(self):
        the_file = self.cleaned_data.get('attachment', None)
        file_types = {
            'application/pdf': '.pdf'
        }
        return clean_file(the_file, file_types)
