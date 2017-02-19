from django.contrib import admin
from .models import Teacher, School, SchoolClass, SchoolClassCode

admin.site.register(School)
admin.site.register(SchoolClass)
admin.site.register(SchoolClassCode)
admin.site.register(Teacher)
