from django.shortcuts import render, redirect

from teachers.models import Invitation
from .forms import StudentSignUpForm
from .models import Student

def signup(request):
    form = StudentSignUpForm()

    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)

        if form.is_valid():
            new_user = form.save(request)
            student = Student.objects.create(
                user=new_user,
                school=form.cleaned_data['school']
            )
            student.save()
            return redirect('homepage')

    context = {
        'form': form
    }
    return render(request, 'students/signup.html', context)
