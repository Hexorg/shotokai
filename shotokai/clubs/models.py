from django.db import models

from member_content.models import Member

import time # for time formatting

class Address(models.Model):
    first_line = models.CharField(max_length=256)
    second_line = models.CharField(null=True, max_length=256, blank=True)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    zip = models.IntegerField()

    def __str__(self):
        return "{}\n{}, {} {}".format(self.first_line, self.city, self.state, "{:05d}".format(self.zip))

class MeetingTime(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY = 'MO', "Monday"
        TUESDAY = 'TU', "Tuesday"
        WEDNESDAY = 'WE', "Wednesday"
        THURSDAY = 'TH', "Thursday"
        FRIDAY = 'FR', "Friday"
        SATURDAY = 'SA', "Saturday"
        SUNDAY = 'SU', "Sunday"
    
    
    day_of_the_week = models.CharField(max_length=2, choices=DayOfWeek.choices, default=DayOfWeek.MONDAY)
    time = models.TimeField("Meeting time")

    def __str__(self):
        return "{} at {}".format(self.DayOfWeek(self.day_of_the_week).label, self.time.strftime("%I:%M %p"))

class Club(models.Model):
    name = models.CharField('Club name', max_length=256, null=True, blank=True)
    instructor = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    meeting_time = models.ManyToManyField(MeetingTime)
    text = models.TextField('Content')

    def __str__(self):
        return self.name if self.name else "{}'s club in {}, {}".format(self.instructor if self.instructor else "No one", self.location.city if self.location else "Undefined", self.location.state if self.location else "NULL")
    

