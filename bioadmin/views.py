from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

from .forms import SchoolForm, CategoryForm
from teachers.models import School
from biobricks.models import Category

@login_required
@staff_member_required
def index(request):
  context = {}
  return render(request, 'bioadmin/index.html', context)

# schools

@login_required
@staff_member_required
def schools(request):
  schools = School.objects.all()
  context = {
      'schools': schools
  }
  return render(request, 'bioadmin/schools.html', context)

@login_required
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

# biobricks

@login_required
@staff_member_required
def biobricks(request):
  categories = Category.objects.all()
  context = {
          'categories': categories
  }
  return render(request, 'bioadmin/biobricks.html', context)

@login_required
@staff_member_required
def new_category(request):
  form = CategoryForm()

  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      category = Category.objects.create(**form.cleaned_data)
      category.save()
      messages.success(request, "You created a category")
      return redirect('bioadmin:biobricks') #fixme

  context = {'form': form}
  return render(request, 'bioadmin/new_category.html', context)
