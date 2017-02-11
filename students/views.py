from django.shortcuts import render

from teachers.models import Invitation
from .forms import StudentSignUpForm

def new_student(request):
    form = StudentSignUpForm()

    if request.method == 'POST':
        invitation = Invitation.objects.get(code=code)
        #if !invitation.has_expired?:

    context = {
        'form': form
    }
    return render(request, 'students/signup.html', context)
