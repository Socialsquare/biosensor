from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, UpdateView

from django.core.urlresolvers import reverse


class EditProfileView(UpdateView):
    model = get_user_model()
    fields = ['first_name', 'last_name']
    template_name = 'users/profile_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse('homepage')


profile = login_required(EditProfileView.as_view())
