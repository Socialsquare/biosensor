from django.contrib import admin
from .models import Teacher, School, Schoolclass, Invitation

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Invitation)
admin.site.register(Schoolclass)
