from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

import hashlib

from .forms import SchoolForm, CategoryForm, BiobrickForm, BiosensorForm
from .tasks import send_school_notice
from teachers.models import School, Teacher
from studentgroups.models import StudentGroup, StudentReport
from biobricks.models import Category, Biobrick, Biosensor

@login_required
@staff_member_required
def index(request):
  context = {}
  return render(request, 'bioadmin/index.html', context)

# teacher overview

@login_required
@staff_member_required
def teachers(request):
  teachers = Teacher.objects.all()
  context = {
      'teachers': teachers,
  }
  return render(request, 'bioadmin/teachers.html', context)

# student group overview

@login_required
@staff_member_required
def student_groups(request):
  student_groups = StudentGroup.objects.all()
  context = {
      'student_groups': student_groups
  }
  return render(request, 'bioadmin/student_groups.html', context)

# schools overview

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
      passwd = User.objects.make_random_password().encode('utf-8')
      school.password = hashlib.sha512(passwd).hexdigest()
      school.save()
      send_school_notice(school, passwd)
      messages.success(request, "You created a school")
      return redirect('bioadmin:schools')

  context = {'form': form}
  return render(request, 'bioadmin/new_school.html', context)

# catalog overview

@login_required
@staff_member_required
def catalog(request):
  biosensors = Biosensor.objects.all()
  detectors = Biobrick.objects.filter(biobrick_type='detector')
  responders = Biobrick.objects.filter(biobrick_type='responder')
  categories = Category.objects.all()
  context = {
          'biosensors': biosensors,
          'detectors': detectors,
          'responders': responders,
          'categories': categories
  }
  return render(request, 'bioadmin/catalog.html', context)

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
      return redirect('bioadmin:catalog') #fixme

  context = {'form': form}
  return render(request, 'bioadmin/category.html', context)

@transaction.atomic
@staff_member_required
@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'GET':
        context = {
                'category': category
                }
        return render(request, 'bioadmin/delete_category.html', context)
    else:
        if category.is_empty() and 'yes' == request.POST.get('confirmation', 'no'):
            category.delete()
            messages.success(request, "You deleted a category")
        return redirect('bioadmin:catalog')

@transaction.atomic
@staff_member_required
@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = CategoryForm({
        'name': category.name,
        'category_type': category.category_type
        })
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category.name = form.cleaned_data['name']
            category.save()
            messages.success(request, "You updated this category")
            return redirect('bioadmin:catalog')

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
    biobrick_type = biobrick_type == 'responsgen' and 'responder' or 'detector'

    if request.method == 'POST':
        form = BiobrickForm(request.POST)
        if form.is_valid():
            biobrick = Biobrick.objects.create(**form.cleaned_data)
            biobrick.biobrick_type = biobrick_type
            biobrick.save()
            messages.success(request, "You created a biobrick")
        return redirect('bioadmin:catalog')

    form.filter_categories(biobrick_type)
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
        return redirect('bioadmin:catalog')

@transaction.atomic
@staff_member_required
@login_required
def edit_biobrick(request, biobrick_id):
    biobrick = get_object_or_404(Biobrick, id=biobrick_id)
    form = BiobrickForm({
        'category': biobrick.category.id,
        'name': biobrick.name,
        'description': biobrick.description,
        'design': biobrick.design,
        'igem_part': biobrick.igem_part,
        'team_website': biobrick.team_website,
        'dna_sequence': biobrick.dna_sequence,
        'coord_x': biobrick.coord_x,
        'coord_y': biobrick.coord_y,
        })
    if request.method == 'POST':
        form = BiobrickForm(request.POST)
        if form.is_valid():
            biobrick.category = form.cleaned_data['category']
            biobrick.name = form.cleaned_data['name']
            biobrick.description = form.cleaned_data['description']
            biobrick.design = form.cleaned_data['design']
            biobrick.igem_part = form.cleaned_data['igem_part']
            biobrick.team_website = form.cleaned_data['team_website']
            biobrick.dna_sequence = form.cleaned_data['dna_sequence']
            biobrick.coord_x = form.cleaned_data['coord_x']
            biobrick.coord_y = form.cleaned_data['coord_y']
            biobrick.save()
            messages.success(request, "You updated this biobrick")
            return redirect('bioadmin:catalog')

    form.filter_categories(biobrick.biobrick_type)
    context = {
            'biobrick': biobrick,
            'biobrick_type': biobrick.biobrick_type,
            'form': form
            }
    return render(request, 'bioadmin/biobrick.html', context)

@login_required
@staff_member_required
def new_biosensor(request):
    form = BiosensorForm()

    if request.method == 'POST':
        form = BiosensorForm(request.POST)
        if form.is_valid():
            biosensor = Biosensor.objects.create(user_id=request.user.id, **form.cleaned_data)
            biosensor.save()
            messages.success(request, "You created a biosensor")
        return redirect('bioadmin:catalog')

    context = {
        'form': form
        }
    return render(request, 'bioadmin/biosensor.html', context)

@login_required
@staff_member_required
def delete_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)

    if request.method == 'GET':
        context = {'biosensor': biosensor}
        return render(request, 'bioadmin/delete_biosensor.html', context)
    else:
        if 'yes' == request.POST.get('confirmation', 'no'):
            biosensor.delete()
            messages.success(request, "You deleted a biosensor")
        return redirect('bioadmin:catalog')

@login_required
@staff_member_required
def edit_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    form = BiosensorForm({
        'name': biosensor.name,
        'detector': biosensor.detector.id,
        'responder': biosensor.responder.id,
        'category': biosensor.category.id,
        'problem_description': biosensor.problem_description,
        'risk_description': biosensor.risk_description
        })
    if request.method == 'POST':
        form = BiosensorForm(request.POST)
        if form.is_valid():
            biosensor.name = form.cleaned_data['name']
            biosensor.detector = form.cleaned_data['detector']
            biosensor.responder = form.cleaned_data['responder']
            biosensor.category = form.cleaned_data['category']
            biosensor.problem_description = form.cleaned_data['problem_description']
            biosensor.risk_description = form.cleaned_data['risk_description']
            biosensor.save()
            messages.success(request, "You updated this biosensor")
            return redirect('bioadmin:catalog')

    context = {
            'biosensor': biosensor,
            'form': form
            }
    return render(request, 'bioadmin/biosensor.html', context)

def show_biosensor(request, biosensor_id):
    biosensor = get_object_or_404(Biosensor, id=biosensor_id)
    detector = Biobrick.objects.get(id=biosensor.detector.id)
    responder = Biobrick.objects.get(id=biosensor.responder.id)
    student_reports = StudentReport.objects.filter(biosensor=biosensor)
    context = {
            'biosensor': biosensor,
            'detector': detector,
            'responder': responder,
            'student_reports': student_reports,
            }
    return render(request, 'bioadmin/show_biosensor.html', context)

def show_student_report(request, report_id):
    report = get_object_or_404(StudentReport, id=report_id)
    context = {
            'report': report,
            }
    return render(request, 'bioadmin/show_student_report.html', context)



