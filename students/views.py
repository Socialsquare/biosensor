from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from allauth.account.utils import complete_signup

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
                school_class=form.cleaned_data['school_class']
            )
            student.save()
            return complete_signup(
                request,
                new_user,
                settings.ACCOUNT_EMAIL_VERIFICATION,
                reverse('account_email_verification_sent')
            )

    context = {
        'form': form
    }
    return render(request, 'students/signup.html', context)
