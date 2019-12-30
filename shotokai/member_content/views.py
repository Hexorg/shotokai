from django.shortcuts import render, redirect

# Create your views here.


def register(request):
    from django.contrib.auth import login, authenticate
    from .forms import SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'member_content/register.html', {'form': form})

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
            return redirect('index')
        else:
            return render(request, 'member_content/login_failed.html', {'login_form':form})
        
    
    from django.http import HttpResponseBadRequest
    return HttpResponseBadRequest("Only POST request allowed here")
    
