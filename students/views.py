from django.shortcuts import render, redirect
from django.contrib import messages

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
            msg = "Velkommen til biosensor. Tjek %s for at bekræfte din konto." % form.cleaned_data['email']
            messages.success(request, msg)
            return redirect('homepage')

    context = {
        'form': form
    }
    return render(request, 'students/signup.html', context)