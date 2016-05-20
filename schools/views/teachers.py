from django.shortcuts import render

from ..models import Teacher
from ..forms import TeacherSignupForm

def signup_teacher(request):
    form = TeacherSignupForm()
    if request.method == 'POST':
        form = TeacherSignupForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['confirmation_key']
            teacher = Teacher.objects.create(**form.cleaned_data)
            teacher.save()
            return redirect('/') #fixme
    context = {
        'form': form
    }
    return render(request, 'schools/signup_teacher.html', context)

