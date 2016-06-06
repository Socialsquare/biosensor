from django.shortcuts import render
from biobricks.models import Biobrick, Biosensor

def homepage(request):
    detectors = Biobrick.objects.filter(biobrick_type='detector')
    responders = Biobrick.objects.filter(biobrick_type='responder')
    biosensors = Biosensor.objects.all()
    context = {
            'detectors': detectors,
            'responders': responders,
            'biosensors': biosensors,
    }
    return render(request, 'index.html', context)
