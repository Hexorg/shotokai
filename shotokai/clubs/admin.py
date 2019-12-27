from django.contrib import admin

# Register your models here.
from .models import Address, Club, MeetingTime
admin.site.register(Address)
admin.site.register(Club)
admin.site.register(MeetingTime)