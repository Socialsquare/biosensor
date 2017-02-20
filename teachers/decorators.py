from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from teachers.models import is_teacher, Teacher
from studentgroups.models import StudentGroup

teacher_required = user_passes_test(lambda u: u.is_teacher(),
        login_url='/', redirect_field_name=None)


def teaches_student_group(func):
    def check_and_call(request, *args, **kwargs):
        pk = kwargs["student_group_id"]
        group = StudentGroup.objects.get(pk=pk)
        requesting_teacher = Teacher.objects.get(user=request.user)
        if not (group.school_class.school.id == requesting_teacher.school.id):
            return HttpResponse("It is not yours! You are not permitted !",
                                content_type="application/json",
                                status=403)
        return func(request, *args, **kwargs)
    return check_and_call
