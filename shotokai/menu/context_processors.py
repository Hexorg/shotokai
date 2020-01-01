
from django.urls import reverse

from .models import ToplevelEntry
from static_pages import models as page_models

def menu_data(request):
    menu_mapping = {'Clubs': reverse('clubs:index'),
                    'Courses': reverse('courses:index')}

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
        elif menu.text in menu_mapping:
                entries.append({'href':menu_mapping[menu.text], 'text':menu.text})


    # entries = [{'dropdown':practice_entries, 'text':"Practice"},
    #             {'href':reverse('clubs:index'), 'text':"Clubs"},
    #             {'href':"#", 'text':"Courses"},
    #             {'dropdown': organization_entries, 'text':"Organization"},
    #             {'dropdown': media_entries, 'text':"Media"}]

    user_entries = [{'href':reverse('member_content:index'), 'text':'Home'}]
    if request.user.is_staff:
        user_entries.append({'href':reverse('admin:index'), 'text':'Admin interface'})
    menu = {'entries': entries, 'user_entries': user_entries, 'login':'user/login'}
    return {'menu':menu}