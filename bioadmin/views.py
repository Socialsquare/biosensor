from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .forms import SchoolForm
from schools.models import School

@staff_member_required
def index(request):
  context = {}
  return render(request, 'bioadmin/index.html', context)

@staff_member_required
def schools(request):
  schools = School.objects.all()
  context = {
      'schools': schools
  }
  return render(request, 'bioadmin/schools.html', context)

@staff_member_required
def new_school(request):
  form = SchoolForm()

  if request.method == 'POST':
    form = SchoolForm(request.POST)
    if form.is_valid():
      school = School.objects.create(**form.cleaned_data)
      school.save()
      messages.success(request, "You created a school")
      return redirect('/bio-admin/schools/') #fixme

  context = {'form': form}
  return render(request, 'bioadmin/new_school.html', context)
