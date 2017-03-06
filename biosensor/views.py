from django.shortcuts import render
from content.models import ContentPage
from biobricks.models import Category, Biobrick, Biosensor


def homepage(request):
    try:
        frontpage = ContentPage.objects.get(slug='front')
    except ContentPage.DoesNotExist as e:
        frontpage = {
            'body': 'Fejl: Velkomstteksten til forsiden mangler!'
        }

    d_categories = Category.objects.filter(category_type='detector')
    r_categories = Category.objects.filter(category_type='responder')
    biosensors = Biosensor.objects.exclude(
        student_report__resume__exact=''
    ).exclude(
        student_report__image__isnull=True
    ).order_by('name')

    context = {
        'frontpage': frontpage,
        'd_categories': d_categories,
        'r_categories': r_categories,
        'biosensors': biosensors
    }
    return render(request, 'index.html', context)
