from allauth.account.forms import LoginForm

def login_form_processor(request):
    login_form = LoginForm()
    return {'login_form': login_form}
