from django.contrib import admin

# Register your models here.
from .models import Club, MeetingTime
admin.site.register(Club, list_display = ['name', 'instructor', 'location'])
admin.site.register(MeetingTime)