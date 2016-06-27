from django.shortcuts import render
from biobricks.models import Category, Biobrick, Biosensor

def homepage(request):
    d_categories = Category.objects.filter(category_type='detector')
    r_categories = Category.objects.filter(category_type='responder')
    b_categories = Category.objects.filter(category_type='biosensor')
    context = {
            'd_categories': d_categories,
            'r_categories': r_categories,
            'b_categories': b_categories,
    }
    return render(request, 'index.html', context)
