from django import forms

class AddBlogForm(forms.Form):
    topic = forms.CharField(required=True)
    text = forms.CharField(required=True, widget=forms.Textarea)