from .forms import MenuLoginForm

def login_form(request):
        return {'login_form':MenuLoginForm()}