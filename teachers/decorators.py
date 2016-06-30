from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from teachers.models import is_teacher
from studentgroups.models import StudentGroup

teacher_required = user_passes_test(lambda u: u.is_teacher(),
        login_url='/', redirect_field_name=None)

def owns_student_group(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["student_group_id"]
        group = StudentGroup.objects.get(pk=pk)
        if not (group.teacher.user.id == request.user.id):
            return HttpResponse("It is not yours ! You are not permitted !",
                        content_type="application/json", status=403)
        return func(request, *args, **kwargs)
    return check_and_call
