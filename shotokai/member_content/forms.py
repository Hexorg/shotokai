from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Member

class BootstrapUserCreationForm(UserCreationForm):
    class Meta:
        textWidget = forms.TextInput(attrs={'class':'form-control'})
        passwdWidget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})

        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1',  'password2')
        widgets = {
            'username': textWidget,
            'email': textWidget,
            'password1': passwdWidget,
            'password2': passwdWidget,
            'first_name': textWidget,
            'last_name': textWidget,
        }

class MenuLoginForm(AuthenticationForm):
    usernameWidget = forms.TextInput(attrs={'class':'form-control'})
    passwdWidget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = self.passwdWidget
        self.fields['username'].widget = self.usernameWidget

class MemberCreationForm(forms.ModelForm):
    def save(self, commit=True):
        import datetime
        self.instance.paid_until = datetime.date.today() - datetime.timedelta(days=1)
        return super().save(commit)
    class Meta:
        beltWidget = forms.Select(attrs={'class':'form-control'})
    

        model = Member
        fields = ('belt', 'picture', 'bio')
        widgets = {
            'belt': beltWidget,
            'picture': beltWidget,
        }