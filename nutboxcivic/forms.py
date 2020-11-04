from django import forms
from masterdata.models import Emailtemplate
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