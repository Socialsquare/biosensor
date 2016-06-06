from django.contrib.auth.decorators import user_passes_test
from teachers.models import is_teacher

teacher_required = user_passes_test(lambda u: u.is_teacher(),
        login_url='/', redirect_field_name=None)
