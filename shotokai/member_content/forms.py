from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Member


class MenuLoginForm(AuthenticationForm):
    usernameWidget = forms.TextInput(attrs={'class':'form-control'})
    passwdWidget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = self.passwdWidget
        self.fields['username'].widget = self.usernameWidget

class SignUpForm(UserCreationForm):
    usernameWidget = forms.TextInput(attrs={'class':'form-control'})
    textWidget = forms.TextInput(attrs={'class':'form-control'})
    emailWidget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'you@example.com'})
    beltWidget = forms.Select(attrs={'class':'form-control'})
    passwdWidget = forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'})

    first_name = forms.CharField(max_length=30, required=True, help_text='Requred for billing', widget=textWidget)
    last_name = forms.CharField(max_length=30, required=True,  help_text='Requred for billing', widget=textWidget)
    email = forms.EmailField(max_length=254, help_text='We will send you notifications and reminders.', widget=emailWidget)
    belt = forms.ChoiceField(choices=Member.Belt.choices, required=True, initial=Member.Belt.WHITE, help_text="If you are unsure, choose White", widget=beltWidget)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = self.passwdWidget
        self.fields['password2'].widget = self.passwdWidget
        self.fields['username'].widget = self.usernameWidget

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'belt',)
    
    def save(self, commit=True):
        import datetime
        user = super().save(commit=False)
        print(type(user))
        m = Member(user=user, belt=self.cleaned_data.get('belt'), paid_until=datetime.date.today())
        if commit:
            user.save()
            m.save()
        return user