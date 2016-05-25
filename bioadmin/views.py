from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db import transaction

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
  return render(request, 'bioadmin/category.html', context)

@transaction.atomic
@staff_member_required
@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'GET':
        context = {'category': category}
        return render(request, 'bioadmin/delete_category.html', context)
    else:
        if 'yes' == request.POST.get('confirmation', 'no'):
            category.delete()
            messages.success(request, "You deleted a category")
        return redirect('bioadmin:biobricks')

@transaction.atomic
@staff_member_required
@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.category_type = form.cleaned_data['category_type']
            category.save()
            messages.success(request, "You updated this category")
            return redirect('bioadmin:biobricks')

    form = CategoryForm({
        'name': category.name,
        'category_type': category.category_type
        })
    context = {'category': category, 'form': form}
    return render(request, 'bioadmin/category.html', context)
