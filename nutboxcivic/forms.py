from django import forms
from masterdata.models import Emailtemplate, client, Representative
from django.contrib.auth.models import User
class templateForm(forms.ModelForm):
    class Meta:
        model = Emailtemplate
        fields = ('title', 'shortDescription','contentTemp', 'subject', 'state')
        widgets = {
            'title' : forms.TextInput(attrs = {'class': 'form-control'}),
            'shortDescription' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'contentTemp' : forms.Textarea(attrs = {'class' : 'form-control'}),
            'subject' : forms.TextInput(attrs = {'class' : 'form-control'}),
            'state' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = client
        fields = ('State','representatives')
        widgets = {
            'State' : forms.TextInput(attrs = {'class': 'form-control'}),
        }
        representatives = forms.ModelChoiceField(queryset=Representative.objects.all().order_by('state'))