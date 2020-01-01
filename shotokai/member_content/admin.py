from django.contrib import admin
from django.utils.html import format_html

from django.urls import reverse
import datetime

from .models import Member
# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'current_belt', 'associated_instructor', 'member_until', 'edit_user_data')

    def email(self, member):
        return member.user.email
    
    def member_until(self, member):
        ''' Color field red if Member is not paid
                Orange if membership expires within a week
                black otherwise'''
        color = "black"
        diff = member.days_until_need_to_pay()
        if diff < 0:
            color = "red"
        elif diff < 8:
            color = "orange"
        else:
            color = "black"
        return format_html('<font color="{}">{}</font>', color, member.paid_until)

    def current_belt(self, member):
        return member.html_belt()
    
    def edit_user_data(self, member):
        ''' Provides a link to user data, where admin can reset passwords'''
        link = reverse("admin:auth_user_change", args=[member.user.id])
        return format_html('<a href="{}">{}</a>', link, member.user)

        
