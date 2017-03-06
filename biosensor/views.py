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
    biosensors = Biosensor.objects.all().order_by('name')

    # We're mocking a category, so we can use the same logic when rendering
    b_categories = [{
        'name': 'Alle',
        'items': biosensors,
        'category_type': 'biosensor'
    }]
    context = {
            'frontpage': frontpage,
            'd_categories': d_categories,
            'r_categories': r_categories,
            'b_categories': b_categories
    }
    return render(request, 'index.html', context)
