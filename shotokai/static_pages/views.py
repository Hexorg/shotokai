from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return render(request, 'index_page/base_template.html', {'site_name': "Hexorg's Blog"})
