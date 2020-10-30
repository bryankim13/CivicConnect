from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from masterdata.models import Emailtemplate

import urllib #to encode email templates into url format for the mailto url link
#urllib.unquote(selectedtemplatecontent.value).decode('utf8')


class homeView(generic.TemplateView):
    template_name = 'civic/home.html'


def usetemplate(request):
    
   # if request.method == 'POST':
    #    form = YourForm(request.POST)
     #   if form.is_valid():
      #      answer = form.cleaned_data['value']
       #     return render(request, 'civic/send.html', {
        #    'templates_all': Emailtemplate.objects.all(),
         #   'chosentemplate' : request.GET ,
          #  })
    #else:
    selectedtemplateid = ''
    selectedtemplatecontent = ''
    link = ''
    emails = 'leyew99290@ofdyn.com' # a temporary email 
    if len(request.GET) > 0:
        selectedtemplateid = request.GET['templatedropdown']
        selectedtemplatecontent = Emailtemplate.objects.get(id = selectedtemplateid).contentTemp
        link = 'mailto:' + emails + '?cc=&subject=' + urllib.parse.quote(Emailtemplate.objects.get(id = selectedtemplateid).subject) + '&body=' + urllib.parse.quote(selectedtemplatecontent)
    return render(request, 'civic/send.html', {
        'templates_all': Emailtemplate.objects.all(),
        'chosentemplate' : selectedtemplatecontent ,
        'generatedlink' : link,
    })

def selecttemplate(request):
    statefilter = ''
    issuefilter = ''
    if len(request.GET) > 0:
        statefilter = ''
        issuefilter = ''
    return render(request, 'civic/templateselection.html', {
        'templates_all': Emailtemplate.objects.all(),
        'sfilter' : statefilter ,
        'ifilter' : issuefilter,
    })