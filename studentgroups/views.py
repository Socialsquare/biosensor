from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import BiosensorForm
from .decorators import student_group_required
from biobricks.models import Biosensor

@login_required
@student_group_required
def dashboard(request):
    biosensors = Biosensor.objects.filter(user=request.user)
    context = {
            'biosensors': biosensors
            }
    return render(request, 'studentgroups/dashboard.html', context)

@login_required
@student_group_required
def new_biosensor(request):
    form = BiosensorForm()

    if request.method == 'POST':
        form = BiosensorForm(request.POST)
        if form.is_valid():
            biosensor = Biosensor.objects.create(user_id=request.user.id, **form.cleaned_data)
            biosensor.save()
            messages.success(request, "Du har oprettet en biosensor")
        return redirect('studentgroups:dashboard')

    context = {
        'form': form
        }
    return render(request, 'studentgroups/biosensor.html', context)

@login_required
@student_group_required
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
@student_group_required
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
