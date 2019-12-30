from django.contrib import admin

# Register your models here.
from .models import Address, Club, MeetingTime
admin.site.register(Address, list_display = ['first_line', 'city', 'state', 'zip'])
admin.site.register(Club, list_display = ['name', 'instructor', 'location'])
admin.site.register(MeetingTime)