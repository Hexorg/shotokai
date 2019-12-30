from django.contrib import admin

from .models import Member
# Register your models here.

admin.site.register(Member, list_display = ['__str__', 'belt', 'paid_until'])