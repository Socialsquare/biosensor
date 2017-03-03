from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404

from allauth.account.utils import complete_signup
import hashlib

from .models import Teacher, School, SchoolClass, SchoolClassCode
from studentgroups.models import StudentGroup, StudentReport
from .forms import TeacherSignupForm, StudentGroupForm, SchoolClassForm
from .decorators import teacher_required, teaches_student_group
from .tasks import send_student_group_notice


def signup(request):
    form = TeacherSignupForm()
    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(request)  # allauth creates a new user
            teacher = Teacher.objects.create(
                    user=new_user,
                    school=form.cleaned_data['school'],
                    subjects=form.cleaned_data['subjects'])
            teacher.save()
            return complete_signup(
                request,
                new_user,
                settings.ACCOUNT_EMAIL_VERIFICATION,
                reverse('account_email_verification_sent')
            )
    context = {
        'form': form
    }
    return render(request, 'teachers/signup.html', context)


@login_required
@teacher_required
def dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    school_classes = SchoolClass.objects.filter(school=teacher.school)
    context = {
        'school_classes': school_classes
    }
    return render(request, 'teachers/dashboard.html', context)


@login_required
@teacher_required
def new_school_class(request):
    form = SchoolClassForm()

    if request.method == 'POST':
        form = SchoolClassForm(request.POST)
        school = Teacher.objects.get(user=request.user).school
        if form.is_valid():
            school_class = SchoolClass.objects.create(
                enrollment_year=form.cleaned_data['enrollment_year'],
                letter=form.cleaned_data['letter'],
                study_field=form.cleaned_data['study_field'],
                school=school
            )

            school_class.save()

            return redirect('teachers:dashboard')
    context = {'form': form}
    return render(request, 'teachers/new_school_class.html', context)


@login_required
@teacher_required
def show_school_class(request, school_class_id):
    school_class = get_object_or_404(SchoolClass, id=school_class_id)
    student_groups = school_class.student_groups
    student_groups = student_groups.order_by('name')
    code_expired = school_class.school_class_code.has_expired if(
        hasattr(school_class, 'school_class_code')
    ) else False
    
    context = {
        'school_class': school_class,
        'student_groups': student_groups,
        'code_expired': code_expired
    }
    return render(request, 'teachers/show_school_class.html', context)


@login_required
@teacher_required
def new_student_group(request, school_class_id):
    school_class = get_object_or_404(SchoolClass, id=school_class_id)
    form = StudentGroupForm(school_class=school_class)
    if request.method == 'POST':
        form = StudentGroupForm(request.POST, school_class=school_class)
        if form.is_valid():
            student_group = StudentGroup.objects.create(
                name=form.cleaned_data['name'],
                school_class=school_class
            )
            student_group.save()
            student_pks = [student.pk for student in form.cleaned_data['students']]
            student_group.students.add(*student_pks)
            send_student_group_notice(student_group)
            return redirect('teachers:show_school_class', school_class.id)

    context = {
        'school_class': school_class,
        'form': form
    }
    return render(request, 'teachers/student_group.html', context)


@login_required
@teaches_student_group
def delete_student_group(request, school_class_id, student_group_id):
    school_class = get_object_or_404(SchoolClass, id=school_class_id)
    student_group = get_object_or_404(StudentGroup, id=student_group_id)

    if request.method == 'GET':
        context = {
            'student_group': student_group
        }
        return render(request, 'teachers/delete_student_group.html', context)
    else:
        if 'yes' == request.POST.get('confirmation', 'no'):
            student_group.delete()
            messages.success(request, "Du har slettet elevgruppen")
        return redirect('teachers:show_school_class', school_class.id)


@login_required
@teaches_student_group
def edit_student_group(request, school_class_id, student_group_id):
    school_class = get_object_or_404(SchoolClass, id=school_class_id)
    student_group = get_object_or_404(StudentGroup, id=student_group_id)
    attributes = {
        'group_id': student_group.id,
        'name': student_group.name,
        'students': student_group.students.all()
    }
    form = StudentGroupForm(attributes, school_class=school_class)
    if request.method == 'POST':
        form = StudentGroupForm(request.POST, school_class=school_class)
        if form.is_valid():
            student_group.name = form.cleaned_data['name']
            student_group.students = form.cleaned_data['students']
            student_group.save()
            messages.success(request, "Dine ændringer er gemt")
            return redirect('teachers:show_school_class', school_class.id)

    context = {
        'student_group': student_group,
        'school_class': school_class,
        'form': form
    }
    return render(request, 'teachers/student_group.html', context)


@login_required
@teacher_required
def show_student_report(request, report_id):
    report = get_object_or_404(StudentReport, id=report_id)
    context = {
            'report': report,
            }
    return render(request, 'teachers/show_student_report.html', context)


@login_required
@teacher_required
def new_school_class_code(request, school_class_id):
    school_class = get_object_or_404(SchoolClass, id=school_class_id)
    if request.method == 'POST':
        # Delete any class codes associated with the school
        SchoolClassCode.objects.filter(school_class=school_class).delete()
        # And then create a new
        school_class_code = SchoolClassCode.create(school_class=school_class)
    return redirect('teachers:show_school_class', school_class.id)
