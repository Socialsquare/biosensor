from django.contrib.auth.decorators import user_passes_test
from studentgroups.models import is_student_group

student_group_required = user_passes_test(lambda u: u.is_student_group(),
        login_url='/', redirect_field_name=None)

