from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    from django.contrib.auth import login, authenticate
    from .forms import MemberCreationForm, BootstrapUserCreationForm
    from location.forms import AddressForm
    form_classes = [BootstrapUserCreationForm, MemberCreationForm, AddressForm]
    form_objects = []
    user, member, address = None, None, None
    if request.method == 'POST':
        for form_class in form_classes:
            form_instance = form_class(data=request.POST)
            form_objects.append(form_instance)
            if form_instance.is_valid():
                if isinstance(form_instance, BootstrapUserCreationForm):
                    user = form_instance.save()
                elif isinstance(form_instance, MemberCreationForm):
                    member = form_instance.save(commit=False)
                elif isinstance(form_instance, AddressForm):
                    address = form_instance.save()
        member.user = user
        member.address = address
        member.save()
        login(request, user)
        return redirect('member_content:index')
    else:
        for form_class in form_classes:
            form_objects.append(form_class())
    return render(request, 'member_content/register.html', {'forms': form_objects})

def logout(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('index')

def login(request):
    from django.contrib.auth import login, authenticate
    from .forms import MenuLoginForm
    if request.method == 'POST':
        form = MenuLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('member_content:index')
        else:
            return render(request, 'member_content/login_failed.html', {'login_form':form})
        
    
    from django.http import HttpResponseBadRequest
    return HttpResponseBadRequest("Only POST request allowed here")
    
@login_required(login_url='/')
def index(request):
    return render(request, 'member_content/index.html')


