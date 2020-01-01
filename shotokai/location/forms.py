from django import forms
from .models import Address

class AddressForm(forms.ModelForm):

    def save(self, commit=True):
        ''' Uses geopy to figure out address' lat and long '''
        from geopy.geocoders import Nominatim
        geolocator = Nominatim(user_agent="shotokai.org site")
        # "{} {}".format(self.first_line, self.second_line) if self.second_line else

        query = {'street': str(self.instance.first_line),
                 'city': str(self.instance.city),
                 'state': Address.State(self.instance.state).label,
                 'country': "United States",
                 'postalcode': "{:05d}".format(self.instance.zip)}

        location = geolocator.geocode(query, country_codes='us')
        if not location:
            del query['city']
            location = geolocator.geocode(query, country_codes='us')
        if not location:
            print(query)

        print("{}: {}".format("location:", location))
        if location:
            self.instance.latitude = location.latitude
            self.instance.longitude = location.longitude
        return super().save(commit)

    class Meta:
        textWidget = forms.TextInput(attrs={'class':'form-control'})
        choiceWidget = forms.Select(attrs={'class':'form-control'})
        intWidget = forms.NumberInput(attrs={'class':'form-control'})

        model = Address
        fields = ('first_line', 'second_line', 'city', 'state', 'zip')
        widgets = {
            'first_line': textWidget,
            'second_line': textWidget,
            'city': textWidget,
            'state': choiceWidget, 
            'zip': intWidget
        }
    