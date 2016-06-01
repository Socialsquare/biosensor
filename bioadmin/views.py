from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms

from .forms import SchoolForm, CategoryForm, BiobrickForm
from teachers.models import School
from biobricks.models import Category, Biobrick

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
      return redirect('bioadmin:schools')

  context = {'form': form}
  return render(request, 'bioadmin/new_school.html', context)

# biobricks

@login_required
@staff_member_required
def biobricks(request):
  categories = Category.objects.all()
  detectors = Biobrick.objects.filter(biobrick_type='detector')
  responders = Biobrick.objects.filter(biobrick_type='responder')
  context = {
          'categories': categories,
          'detectors': detectors,
          'responders': responders
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
    biobricks = Biobrick.objects.filter(category_id=category_id)

    if request.method == 'GET':
        context = {
                'category': category,
                'biobricks': biobricks
                }
        return render(request, 'bioadmin/delete_category.html', context)
    else:
        if not biobricks and 'yes' == request.POST.get('confirmation', 'no'):
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
            category.save()
            messages.success(request, "You updated this category")
            return redirect('bioadmin:biobricks')

    form = CategoryForm({
        'name': category.name,
        'category_type': category.category_type
        })
    # do not allow category to be changed
    form.fields['category_type'].widget = forms.HiddenInput()
    context = {
            'category': category,
            'form': form
            }
    return render(request, 'bioadmin/category.html', context)

@login_required
@staff_member_required
def new_biobrick(request, biobrick_type):
    form = BiobrickForm()
    form.filter_categories(biobrick_type)

    if request.method == 'POST':
        form = BiobrickForm(request.POST)
        if form.is_valid():
            biobrick = Biobrick.objects.create(**form.cleaned_data)
            biobrick.biobrick_type = biobrick_type
            biobrick.save()
            messages.success(request, "You created a biobrick")
        return redirect('bioadmin:biobricks')

    context = {
        'form': form,
        'biobrick_type': biobrick_type
        }
    return render(request, 'bioadmin/biobrick.html', context)

@transaction.atomic
@staff_member_required
@login_required
def delete_biobrick(request, biobrick_id):
    biobrick = get_object_or_404(Biobrick, id=biobrick_id)

    if request.method == 'GET':
        context = {'biobrick': biobrick}
        return render(request, 'bioadmin/delete_biobrick.html', context)
    else:
        if 'yes' == request.POST.get('confirmation', 'no'):
            biobrick.delete()
            messages.success(request, "You deleted a biobrick")
        return redirect('bioadmin:biobricks')

@transaction.atomic
@staff_member_required
@login_required
def edit_biobrick(request, biobrick_id):
    biobrick = get_object_or_404(Biobrick, id=biobrick_id)
    if request.method == 'POST':
        form = BiobrickForm(request.POST)
        if form.is_valid():
            biobrick.category = form.cleaned_data['category']
            biobrick.name = form.cleaned_data['name']
            biobrick.description = form.cleaned_data['description']
            biobrick.design = form.cleaned_data['design']
            biobrick.igem_part_link = form.cleaned_data['igem_part_link']
            biobrick.team_website = form.cleaned_data['team_website']
            biobrick.dna_sequence = form.cleaned_data['dna_sequence']
            biobrick.save()
            messages.success(request, "You updated this biobrick")
            return redirect('bioadmin:biobricks')

    form = BiobrickForm({
        'category': biobrick.category.id,
        'name': biobrick.name,
        'description': biobrick.description,
        'design': biobrick.design,
        'igem_part_link': biobrick.igem_part_link,
        'team_website': biobrick.team_website,
        'dna_sequence': biobrick.dna_sequence,
        })
    form.filter_categories(biobrick.biobrick_type)
    context = {
            'biobrick': biobrick,
            'biobrick_type': biobrick.biobrick_type,
            'form': form
            }
    return render(request, 'bioadmin/biobrick.html', context)
