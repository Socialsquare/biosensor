from django.shortcuts import render
from biobricks.models import Biobrick

def homepage(request):
    detectors = Biobrick.objects.filter(biobrick_type='detector')
    responders = Biobrick.objects.filter(biobrick_type='responder')
    context = {
            'detectors': detectors,
            'responders': responders,
    }
    return render(request, 'index.html', context)
