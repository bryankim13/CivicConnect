#REFERENCES
#Title: Django ModelForm label customization
#Author: QUHO
#Date: 2016 june 10
#Code version: unknown
#URL: https://stackoverflow.com/questions/20986798/django-modelform-label-customization
#Software License: Creative Commons Attribution-ShareAlike
#


from django import forms
from masterdata.models import Emailtemplate, client, Representative
from django.contrib.auth.models import User
class templateForm(forms.ModelForm):
    class Meta:
        model = Emailtemplate
        fields = ('title', 'shortDescription','subject', 'contentTemp',  'state')
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'form-control'}),
            'shortDescription' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'subject' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'contentTemp' : forms.Textarea(attrs = {'class' : 'form-control'}),
            'state' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }
        labels = {
            "title": "Template Title:",
            'shortDescription' : "Short Description:",
            'subject' : "Email Subject:",
            'contentTemp' : "Email Body:",
            'state' : "Relevant state (e.g., VA):",
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs = {'class': 'form-control'}),
            'email' : forms.TextInput(attrs = {'class': 'form-control'}),
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ('State','representatives')
        widgets = {
            'State' : forms.TextInput(attrs = {'class': 'form-control'}),
        }
        representatives = forms.ModelChoiceField(queryset=Representative.objects.all().order_by('state'))