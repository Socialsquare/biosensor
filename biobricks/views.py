from django.shortcuts import render, get_object_or_404
from .models import Biobrick

def show(request, biobrick_id):
    biobrick = get_object_or_404(Biobrick, id=biobrick_id)
    context = { 'biobrick': biobrick}
    return render(request, 'biobricks/show.html', context)
