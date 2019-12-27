from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Club
from .forms import AddBlogForm

def index(request):
    return render(request, 'clubs/index.html', {'clubs': Club.objects.all()}) # pylint: disable=no-member
        

def club(request, club_id):
    try:
        return render(request, 'clubs/club.html', {'club': Club.objects.get(id=club_id)}) # pylint: disable=no-member
    except Club.DoesNotExist: # pylint: disable=no-member
        raise Http404("Post does not exist")
