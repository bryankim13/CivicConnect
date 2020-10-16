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
    a = ""
    b = ''
    if len(request.GET) > 0:
        a = request.GET['templatedropdown']
        b = Emailtemplate.objects.get(id = a).contentTemp
    return render(request, 'civic/send.html', {
        'templates_all': Emailtemplate.objects.all(),
        'chosentemplate' : b ,
    })