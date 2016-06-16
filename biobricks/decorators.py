from django.contrib.auth.decorators import user_passes_test
from studentgroups.models import is_student_group
from django.http import HttpResponseForbidden

from .models import Biosensor
from .forms import BiosensorForm

def is_owner(func):
    def check_and_call(request, *args, **kwargs):
        pk = args[0]
        biosensor = Biosensor.objects.get(pk=pk)
        if not (biosensor.user.id == request.user.id):
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return check_and_call
