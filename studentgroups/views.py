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
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            student_group = StudentGroup.objects.get(user=request.user)
            report = StudentReport.objects.create(
                    student_group=student_group,
                    biosensor=biosensor,
                    **form.cleaned_data)
            report.save()
            messages.success(request, "Du har uplopadet din rapport")
            return redirect(biosensor)

    form = ReportForm()
    context = {
            'biosensor': biosensor,
            'form': form
            }
    return render(request, 'studentgroups/report.html', context)

@login_required
@student_group_required
def edit_report(request, biosensor_id, report_id):
    report = get_object_or_404(StudentReport, id=report_id)
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            report.introduction = form.cleaned_data['introduction']
            report.method = form.cleaned_data['method']
            report.results = form.cleaned_data['results']
            report.discussion = form.cleaned_data['discussion']
            report.conclusion = form.cleaned_data['conclusion']
            report.save()
            messages.success(request, "Dine ændringer er gemt")
            return redirect(report.biosensor)

    form = ReportForm({
        'introduction': report.introduction,
        'method': report.method,
        'results': report.results,
        'discussion': report.discussion,
        'conclusion': report.conclusion
        })
    context = {
            'biosensor': report.biosensor,
            'report': report,
            'form': form
            }
    return render(request, 'studentgroups/report.html', context)
