from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.urlresolvers import reverse

from .models import StudentGroup, StudentReport
from .forms import ResumeForm, PhotoForm, ReportForm
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


@login_required
@student_group_required
def update_photo(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            report, created = StudentReport.objects.get_or_create(
                biosensor=biosensor
            )
            report.image = form.cleaned_data.get('image', None)
            report.save()
            return redirect('studentgroups:dashboard')
    else:
        form = PhotoForm(initial={
            'image': (
                biosensor.student_report.image
                if hasattr(biosensor, 'student_report')
                else ''
            )
        })
    url = reverse('studentgroups:update_photo', args=(biosensor_id, ))
    return render(request, 'studentgroups/update-photo.html', {
        'form': form,
        'submit_text': 'Gem foto',
        'title': 'Opdater foto af %s' % biosensor,
        'url': url
    })


@login_required
@student_group_required
def update_resume(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            report, created = StudentReport.objects.get_or_create(
                biosensor=biosensor
            )
            report.resume = form.cleaned_data['resume']
            report.save()
            return redirect('studentgroups:dashboard')
    else:
        form = ResumeForm(initial={
            'resume': (
                biosensor.student_report.resume
                if hasattr(biosensor, 'student_report')
                else ''
            )
        })
    url = reverse('studentgroups:update_resume', args=(biosensor_id, ))
    return render(request, 'studentgroups/update-form.html', {
        'form': form,
        'submit_text': 'Gem resumé',
        'title': 'Opdater resuméet for %s' % biosensor,
        'url': url
    })


@login_required
@student_group_required
def update_report(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report, created = StudentReport.objects.get_or_create(
                biosensor=biosensor
            )
            report.attachment = form.cleaned_data.get('attachment', None)
            report.save()
            return redirect('studentgroups:dashboard')
    else:
        form = ReportForm(initial={
            'attachment': (
                biosensor.student_report.attachment
                if hasattr(biosensor, 'student_report')
                else ''
            )
        })
    url = reverse('studentgroups:update_report', args=(biosensor_id, ))
    return render(request, 'studentgroups/update-report.html', {
        'form': form,
        'submit_text': 'Gem rapport',
        'title': 'Opdater rapport for %s' % biosensor,
        'url': url
    })
