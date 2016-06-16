from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import StudentGroup, StudentReport
from .forms import ReportForm
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

# student reports

@login_required
@student_group_required
def new_report(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            student_group = StudentGroup.objects.get(user=request.user)
            report = StudentReport.objects.create(student_group=student_group, **form.cleaned_data)
            report.save()
            messages.success(request, "Du har uplopadet din rapport")
            return redirect(biosensor)

    context = {
            'biosensor': biosensor,
            'form': form
            }
    return render(request, 'studentgroups/new_report.html', context)

