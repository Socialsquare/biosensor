from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage

from .models import StudentGroup, StudentReport
from .forms import ReportForm
from .decorators import student_group_required
from biobricks.models import Biosensor


@login_required
@student_group_required
def dashboard(request):
    student_group = request.user.student.student_groups.first()
    context = {
        'student_group': student_group
    }
    return render(request, 'studentgroups/dashboard.html', context)

# student reports


@login_required
@student_group_required
def new_report(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = StudentReport.objects.create(
                    biosensor=biosensor,
                    **form.cleaned_data)
            report.save()
            messages.success(request, "Du har oprettet en rapport")
            return redirect('studentgroups:dashboard')

    context = {
            'biosensor': biosensor,
            'form': form
            }
    return render(request, 'studentgroups/report.html', context)


@login_required
@student_group_required
def edit_report(request, biosensor_id, report_id):
    report = get_object_or_404(StudentReport, id=report_id)
    attributes = {
        'resume': report.resume,
        }
    if report.image and default_storage.exists(report.image.name):
        files = {
                'image': report.image,
                'attachment': report.attachment
                }
    else:
        files = {}
    form = ReportForm(attributes, files)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['image']:
                if report.has_existing_image():
                    default_storage.delete(report.image.name)
                image = form.cleaned_data['image']
            else:
                image = report.image

            if form.cleaned_data['attachment']:
                if report.has_existing_attachment():
                    default_storage.delete(report.attachment.name)
                attachment = form.cleaned_data['attachment']
            else:
                attachment = report.attachment
            report.image = image
            report.attachment = attachment
            report.save()
            messages.success(request, "Dine ændringer er gemt")
            return redirect('studentgroups:dashboard')

    context = {
            'biosensor': report.biosensor,
            'report': report,
            'form': form
            }
    return render(request, 'studentgroups/report.html', context)
