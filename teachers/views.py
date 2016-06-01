from django.shortcuts import render, redirect

from .models import Teacher
from studentgroups.models import StudentGroup
from .forms import TeacherSignupForm, NewStudentGroupForm

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

def dashboard(request):
    studentgroups = StudentGroup.objects.all()
    context = { 'studentgroups': studentgroups }
    return render(request, 'teachers/dashboard.html', context)

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
                    names=form.cleaned_data['names'],
                    no_students=form.cleaned_data['no_students'],
                    subject=form.cleaned_data['subject'],
                    year=form.cleaned_data['year'])
            student_group.save()
            return redirect('teachers:dashboard')
    context = { 'form': form }
    return render(request, 'teachers/new_student_group.html', context)
