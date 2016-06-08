from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Teacher
from studentgroups.models import StudentGroup
from .forms import TeacherSignupForm, NewStudentGroupForm, EditStudentGroupForm
from .decorators import teacher_required

def signup(request):
    form = TeacherSignupForm()
    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request) #allauth creates a new user
            teacher = Teacher.objects.create(
                    user=user,
                    school=form.cleaned_data['school'],
                    subjects=form.cleaned_data['subjects'])
            teacher.save()
            return redirect('homepage')
    context = {
        'form': form
    }
    return render(request, 'teachers/signup.html', context)

@login_required
@teacher_required
def dashboard(request):
    studentgroups = StudentGroup.objects.all()
    context = { 'studentgroups': studentgroups }
    return render(request, 'teachers/dashboard.html', context)

@login_required
@teacher_required
def new_student_group(request):
    form = NewStudentGroupForm()
    if request.method == 'POST':
        form = NewStudentGroupForm(request.POST)
        if form.is_valid():
            user = form.save(request) #allauth creates a new user
            teacher = Teacher.objects.get(user=request.user)
            student_group = StudentGroup.objects.create(
                    user=user,
                    teacher=teacher,
                    name=form.cleaned_data['name'],
                    names=form.cleaned_data['names'],
                    no_students=form.cleaned_data['no_students'],
                    subject=form.cleaned_data['subject'],
                    year=form.cleaned_data['year'])
            student_group.save()
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
            student_group.delete()
            messages.success(request, "Du har slettet en elevgruppe")
        return redirect('teachers:dashboard')

@login_required
@teacher_required
def edit_student_group(request, student_group_id):
    student_group = get_object_or_404(StudentGroup, id=student_group_id)
    if request.method == 'POST':
        form = EditStudentGroupForm(request.POST)
        if form.is_valid():
            student_group.user.email = form.cleaned_data['email']
            student_group.user.save()
            student_group.name = form.cleaned_data['name']
            student_group.names = form.cleaned_data['names']
            student_group.no_students = form.cleaned_data['no_students']
            student_group.subject = form.cleaned_data['subject']
            student_group.year = form.cleaned_data['year']
            student_group.save()
            messages.success(request, "Dine ændringer er gemt")
            return redirect('teachers:dashboard')

    form = EditStudentGroupForm({
        'email': student_group.user.email,
        'name': student_group.name,
        'names': student_group.names,
        'no_students': student_group.no_students,
        'subject': student_group.subject,
        'year': student_group.year
        })
    context = {
            'student_group': student_group,
            'form': form
            }
    return render(request, 'teachers/student_group.html', context)
