from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):

    class Belt(models.TextChoices):
        # format:
        # python constant = 'value that goes into the database', "text representation"
        # values that go into the database have to be 4 characters long
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
    belt = models.CharField(max_length=4, choices=Belt.choices, default=Belt.RED)
    paid_until = models.DateField()

    def __str__(self):

        return "{} {}".format(self.user.first_name if self.user.first_name else self.user, self.user.last_name if self.user.last_name else "")