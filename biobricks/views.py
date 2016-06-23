from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.contrib.auth.decorators import login_required

from .models import Biobrick, Biosensor
from studentgroups.models import StudentGroup, StudentReport
from .forms import BiosensorForm
from .decorators import is_owner

def show(request, slug):
    biobrick = Biobrick.get_biobrick(slug)
    if not biobrick:
        raise Http404

    coords = ['{}{}'.format(b.coord_x, b.coord_y) for b in Biobrick.objects.all()]
    context = {
            'biobrick': biobrick,
            'coords': coords,
            }
    return render(request, 'biobricks/show.html', context)

def show_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    detector = Biobrick.objects.get(id=biosensor.detector.id)
    responder = Biobrick.objects.get(id=biosensor.responder.id)
    student_reports = StudentReport.objects.filter(biosensor=biosensor)
    context = {
            'biosensor': biosensor,
            'detector': detector,
            'responder': responder,
            'student_reports': student_reports
            }
    return render(request, 'biobricks/show_biosensor.html', context)

@login_required
def new_biosensor(request):
    form = BiosensorForm()

    if request.method == 'POST':
        form = BiosensorForm(request.POST)
        if form.is_valid():
            biosensor = Biosensor.objects.create(user_id=request.user.id, **form.cleaned_data)
            biosensor.save()
            if request.user.is_student_group():
                student_group = StudentGroup.objects.get(user=request.user)
                student_group.biosensors.add(biosensor)
            messages.success(request, "Du har oprettet en biosensor")
        return redirect('studentgroups:dashboard')

    context = {
        'form': form
        }
    return render(request, 'studentgroups/biosensor.html', context)

@login_required
@is_owner
def delete_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)

    if request.method == 'GET':
        context = {'biosensor': biosensor}
        return render(request, 'studentgroups/delete_biosensor.html', context)
    else:
        if 'yes' == request.POST.get('confirmation', 'no'):
            biosensor.delete()
            messages.success(request, "You deleted a biosensor")
        return redirect('studentgroups:dashboard')

@login_required
@is_owner
def edit_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    if request.method == 'POST':
        form = BiosensorForm(request.POST)
        if form.is_valid():
            biosensor.name = form.cleaned_data['name']
            biosensor.detector = form.cleaned_data['detector']
            biosensor.responder = form.cleaned_data['responder']
            biosensor.category = form.cleaned_data['category']
            biosensor.problem_description = form.cleaned_data['problem_description']
            biosensor.risk_description = form.cleaned_data['risk_description']
            biosensor.save()
            messages.success(request, "You updated this biosensor")
            return redirect('studentgroups:dashboard')

    form = BiosensorForm({
        'name': biosensor.name,
        'detector': biosensor.detector.id,
        'responder': biosensor.responder.id,
        'category': biosensor.category.id,
        'problem_description': biosensor.problem_description,
        'risk_description': biosensor.risk_description
        })
    context = {
            'biosensor': biosensor,
            'form': form
            }
    return render(request, 'studentgroups/biosensor.html', context)
