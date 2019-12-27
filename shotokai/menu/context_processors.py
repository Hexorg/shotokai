
from django.urls import reverse

from .models import ToplevelEntry
from static_pages import models as page_models

def menu_data(request):
    entries = []
    for menu in ToplevelEntry.objects.all():
        submenu = []
        try:
            pages = page_models.StaticPage.objects.filter(top_level_menu=menu)
            submenu = [{'href': '/page/{}'.format(page.id), 'text':page.menu_caption} for page in pages]
        except page_models.StaticPage.DoesNotExist:
            continue
        if len(submenu):
            entries.append({'dropdown': submenu, 'text':menu.text})
        else:
            entries.append({'href':'#', 'text':menu.text})

    practice_entries = [{'href':"#", 'text':"F.A.Q."},
                        {'href':"#", 'text':"Philosophy"},
                        {'href':"#", 'text':"Body Condition"},
                        {'href':"#", 'text':"Terms and Techniques"},
                        {'href':"#", 'text':"Kata"},
                        {'href':"#", 'text':"Grading"}]
    organization_entries = [{'href':"#", 'text':"Presidency"},
                            {'href':"#", 'text':"Technical group"},
                            {'href':"#", 'text':"Administrative group"},
                            {'href':"#", 'text':"Certified instructors"},
                            {'href':"#", 'text':"Assistant instructors"},
                            {'href':"#", 'text':"Black-Belts"},
                            {'href':"#", 'text':"Visiting Instructors"}]
    media_entries = [{'href':"#", 'text':"Demo Videos"},
                    {'href':"#", 'text':"How to Tie a Karate Gi and Belt"},
                    {'href':"#", 'text':"Newsletter"},
                    {'href':"#", 'text':"KATA: Taikyoku (1-3, Bo, Bokken)"}]

    # entries = [{'dropdown':practice_entries, 'text':"Practice"},
    #             {'href':reverse('clubs:index'), 'text':"Clubs"},
    #             {'href':"#", 'text':"Courses"},
    #             {'dropdown': organization_entries, 'text':"Organization"},
    #             {'dropdown': media_entries, 'text':"Media"}]

    user_entries = [{'href':'#', 'text':'Add Post'}]
    if request.user.is_staff:
        user_entries.append({'href':reverse('admin:index'), 'text':'Admin interface'})
    menu = {'entries': entries, 'user_entries': user_entries, 'login':'user/login'}
    return {'menu':menu}