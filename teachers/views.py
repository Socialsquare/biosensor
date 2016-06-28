from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

import hashlib

from .models import Teacher, School
from studentgroups.models import StudentGroup, StudentReport
from .forms import TeacherSignupForm, StudentGroupForm
from .decorators import teacher_required
from .tasks import send_student_group_notice

def signup(request):
    form = TeacherSignupForm()
    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save(request) #allauth creates a new user
            teacher = Teacher.objects.create(
                    user=new_user,
                    school=form.cleaned_data['school'],
                    subjects=form.cleaned_data['subjects'])
            teacher.save()
            user = authenticate(username=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('homepage')
    context = {
        'form': form
    }
    return render(request, 'teachers/signup.html', context)

@login_required
@teacher_required
def dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    student_groups = StudentGroup.objects.filter(teacher=teacher).order_by('year', 'grade', 'letter', 'name')
    context = {
            'student_groups': student_groups,
            }
    return render(request, 'teachers/dashboard.html', context)

@login_required
@teacher_required
def new_student_group(request):
    form = StudentGroupForm()
    if request.method == 'POST':
        form = StudentGroupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            passwd = User.objects.make_random_password()
            user = User.objects.create_user(
                username,
                form.cleaned_data['email'],
                passwd)
            teacher = Teacher.objects.get(user=request.user)
            student_group = StudentGroup.objects.create(
                    user=user,
                    teacher=teacher,
                    name=form.cleaned_data['name'],
                    students=form.cleaned_data['students'],
                    subject=form.cleaned_data['subject'],
                    grade=form.cleaned_data['grade'],
                    letter=form.cleaned_data['letter'],
                    year=form.cleaned_data['year'])
            student_group.save()
            send_student_group_notice(
                    student_group.name,
                    student_group.user.email,
                    passwd)
            return redirect('teachers:dashboard')

    context = { 'form': form }
    return render(request, 'teachers/student_group.html', context)

@login_required
@teacher_required
def delete_student_group(request, student_group_id):
    student_group = get_object_or_404(StudentGroup, id=student_group_id)

    if request.method == 'GET':
        context = {'student_group': student_group}
        return render(request, 'teachers/delete_student_group.html', context)
    else:
        if 'yes' == request.POST.get('confirmation', 'no'):
            student_group.user.delete()
            student_group.delete()
            messages.success(request, "Du har slettet en elevgruppe")
        return redirect('teachers:dashboard')

@login_required
@teacher_required
def edit_student_group(request, student_group_id):
    student_group = get_object_or_404(StudentGroup, id=student_group_id)
    attributes = {
        'group_id': student_group.id,
        'email': student_group.user.email,
        'name': student_group.name,
        'students': student_group.students,
        'subject': student_group.subject,
        'grade': student_group.grade,
        'letter': student_group.letter,
        'year': student_group.year
        }
    form = StudentGroupForm(attributes)
    if request.method == 'POST':
        form = StudentGroupForm(request.POST)
        if form.is_valid():
            student_group.user.email = form.cleaned_data['email']
            student_group.user.save()
            student_group.name = form.cleaned_data['name']
            student_group.students = form.cleaned_data['students']
            student_group.subject = form.cleaned_data['subject']
            student_group.grade = form.cleaned_data['grade']
            student_group.letter = form.cleaned_data['letter']
            student_group.year = form.cleaned_data['year']
            student_group.save()
            messages.success(request, "Dine ændringer er gemt")
            return redirect('teachers:dashboard')

    context = {
            'student_group': student_group,
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
