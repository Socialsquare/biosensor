from django.shortcuts import render, get_object_or_404
from .models import Biobrick, Biosensor

def show(request, biobrick_id):
    biobrick = get_object_or_404(Biobrick, id=biobrick_id)
    context = { 'biobrick': biobrick}
    return render(request, 'biobricks/show.html', context)

def show_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    detector = Biobrick.objects.get(id=biosensor.detector.id)
    responder = Biobrick.objects.get(id=biosensor.responder.id)
    context = {
            'biosensor': biosensor,
            'detector': detector,
            'responder': responder
            }
    return render(request, 'biobricks/show_biosensor.html', context)
