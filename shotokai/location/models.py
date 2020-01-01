from django.db import models

# Create your models here.
class Address(models.Model):
    class State(models.TextChoices):
        Alabama = 'AL', "Alabama"
        Alaska = 'AK', "Alaska"
        Arizona = 'AZ', "Arizona"
        Arkansas = 'AR', "Arkansas"
        California = 'CA', "California"
        Colorado = 'CO', "Colorado"
        Connecticut = 'CT', "Connecticut"
        WashingtonDC = 'DC', "Washington, D.C."
        Delaware = 'DE', "Delaware"
        Florida = 'FL', "Florida"
        Georgia = 'GA', "Georgia"
        Hawaii = 'HI', "Hawaii"
        Idaho = 'ID', "Idaho"
        Illinois = 'IL', "Illinois"
        Indiana = 'IN', "Indiana"
        Iowa = 'IA', "Iowa"
        Kansas = 'KS', "Kansas"
        Kentucky = 'KY', "Kentucky"
        Louisiana = 'LA', "Louisiana"
        Maine = 'ME', "Maine"
        Maryland = 'MD', "Maryland"
        Massachusetts = 'MA', "Massachusetts"
        Michigan = 'MI', "Michigan"
        Minnesota = 'MN', "Minnesota"
        Mississippi = 'MS', "Mississippi"
        Missouri = 'MO', "Missouri"
        Montana = 'MT', "Montana"
        Nebraska = 'NE', "Nebraska"
        Nevada = 'NV', "Nevada"
        NewHampshire = 'NH', "New Hampshire"
        NewJersey = 'NJ', "New Jersey"
        NewMexico = 'NM', "New Mexico"
        NewYork = 'NY', "New York"
        NorthCarolina = 'NC', "North Carolina"
        NorthDakota = 'ND', "North Dakota"
        Ohio = 'OH', "Ohio"
        Oklahoma = 'OK', "Oklahoma"
        Oregon = 'OR', "Oregon"
        Pennsylvania = 'PA', "Pennsylvania"
        RhodeIsland = 'RI', "Rhode Island"
        SouthCarolina = 'SC', "South Carolina"
        SouthDakota = 'SD', "South Dakota"
        Tennessee = 'TN', "Tennessee"
        Texas = 'TX', "Texas"
        Utah = 'UT', "Utah"
        Vermont = 'VT', "Vermont"
        Virginia = 'VA', "Virginia"
        Washington = 'WA', "Washington"
        WestVirginia = 'WV', "West Virginia"
        Wisconsin = 'WI', "Wisconsin"
        Wyoming = 'WY', "Wyoming"


    first_line = models.CharField(max_length=256)
    second_line = models.CharField(null=True, max_length=256, blank=True)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=2, choices=State.choices)
    zip = models.IntegerField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return "{}\n{},{} {}".format(self.first_line, self.city, self.state, "{:05d}".format(self.zip))
