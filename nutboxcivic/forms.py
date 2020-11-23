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
            "title": "Email template title",
            'shortDescription' : "Short description of the email template",
            'subject' : "Subject of the email",
            'contentTemp' : "Body of the email",
            'state' : "Relevant State for the contents of the email template",
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