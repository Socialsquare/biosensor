from django.shortcuts import render, redirect

from ..models import Teacher
from ..forms import TeacherSignupForm

def signup_teacher(request):
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
    return render(request, 'schools/signup_teacher.html', context)

