from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.db.models import Q
import datetime


class Member(models.Model):
    class Belt(models.TextChoices):
        # format:
        # python constant = 'value that goes into the database', "text representation"
        # values that go into the database have to be 4 characters long
        WHITE = 'WHT5', "White: 5Th Kyu"
        RED = 'RED4', "Red: 4Th Kyu"
        ORANGE = 'ORNG', "Orange: 3Rd Kyu"
        GREEN = 'GRN2', "Green: 2nd Kyu"
        BROWN = 'BRWN', "Brown: 1st Kyu"
        BLACK1 = 'BLK1', "Black: 1st Dan"
        BLACK2 = 'BLK2', "Black: 2nd Dan"
        BLACK3 = 'BLK3', "Black: 3rd Dan"
        BLACK4 = 'BLK4', "Black: 4th Dan"
        BLACK5 = 'BLK5', "Black: 5th Dan"
    

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.OneToOneField('location.Address', on_delete=models.SET_NULL, null=True, blank=True)
    picture = models.FilePathField(path='member_content/media/', max_length=256, blank=True, null=True)
    belt = models.CharField(max_length=4, choices=Belt.choices, default=Belt.RED)
    associated_instructor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    paid_until = models.DateField()
    bio = models.TextField(blank=True, null=True)

    def html_belt(self):
        ''' Adds a little color box next to the belt name'''
        color = "white"
        if self.belt == Member.Belt.WHITE:
            color = "white"
        elif self.belt == Member.Belt.RED:
            color = "red"
        elif self.belt == Member.Belt.ORANGE:
            color = "orange"
        elif self.belt == Member.Belt.GREEN:
            color = "green"
        else:
            color = "black"
        return format_html('<div style="display:inline-block; width:8px; height:8px; background-color:{}; border:1px solid black;"></div> {}', color, Member.Belt(self.belt).label)

    def clubs(self):
        from clubs.models import Club
        return Club.objects.filter(Q(instructor = self) | Q(instructor = self.associated_instructor))

    def days_until_need_to_pay(self):
        return (self.paid_until - datetime.date.today()).days


    def __str__(self):
        return "{} {}".format(self.user.first_name if self.user.first_name else self.user, self.user.last_name if self.user.last_name else "")

