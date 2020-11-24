#REFERENCES
#Title: Python, remove all non-alphabet chars from string
#Author: limasxgoesto0, Jon-Eric
#Date: 2019 december 18
#Code version: unknown
#URL: https://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string
#Software License: Creative Commons Attribution-ShareAlike
#
#Title: Convert spaces to %20 in list
#Author: Jan Rozycki, Ry-♦
#Date: 2019 dec 22
#Code version: unknown
#URL: https://stackoverflow.com/questions/27556134/convert-spaces-to-20-in-list
#Software License: Creative Commons Attribution-ShareAlike
#
#Title: How do I get a substring of a string in Python?
#Author: Paolo Bergantino, community
#Date: 2017 may 23
#Code version: unknown
#URL: https://stackoverflow.com/questions/663171/how-do-i-get-a-substring-of-a-string-in-python
#Software License: Creative Commons Attribution-ShareAlike
#
#Title: Django request.GET
#Author: tux21b
#Date: 2010 aug 17
#Code version: unknown
#URL: https://stackoverflow.com/questions/3500859/django-request-get
#Software License: Creative Commons Attribution-ShareAlike
#
#Title: How do I pass a URL with multiple parameters into a URL?
#Author: Dexter, Community♦
#Date: 2017 may 23
#Code version: unknown
#URL: https://stackoverflow.com/questions/5095887/how-do-i-pass-a-url-with-multiple-parameters-into-a-url
#Software License: Creative Commons Attribution-ShareAlike
#
#Title: Check if request.GET var is None?
#Author: Wesley
#Date: 2010 mar 11
#Code version: unknown
#URL: https://stackoverflow.com/questions/2422055/how-to-check-if-request-get-var-is-none
#Software License: Creative Commons Attribution-ShareAlike
#

from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from masterdata.models import Emailtemplate, Issue, Representative, client
from .forms import templateForm, UserForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction

import requests
import json
import re

import urllib #to encode email templates into url format for the mailto url link
#urllib.unquote(selectedtemplatecontent.value).decode('utf8')


def homeView(request):
    template_name = 'civic/home.html'
    return render(request, template_name, {
        'templates_all': Emailtemplate.objects.all().order_by('-datecreated')[:5],
    })

class formTemplate(generic.CreateView):
    form_class = templateForm
    model = Emailtemplate
    template_name = 'civic/createTemp.html'

class thanksView(generic.TemplateView):
    template_name = 'civic/thankyou.html'

def showFavorite(request):
    statefilter = ''
    issuefilter = ''
    if len(request.GET) > 0:
        statefilter = ''
        issuefilter = ''
    return render(request, 'civic/favoriteTemplates.html', {
        'templates_all': request.user.clients.favorites.all(),
        'sfilter' : statefilter ,
        'ifilter' : issuefilter,
    })

def formingTemp(request):
    if request.method == "POST":
        form = templateForm(request.POST)
        if form.is_valid():
            emTemp = form.save(commit=False)
            emTemp.save()
    return HttpResponseRedirect(reverse('thanksSubmit'))


def usetemplate(request, templateid):
    if not request.user.is_authenticated:
        return render(request, 'civic/send.html', {
        'noclient': True,
    })
    linkornot = 0
    me = client.objects.get(user = request.user)
    try:
        if(templateid == 0):
            currenttemplate = None
        else:
            currenttemplate = Emailtemplate.objects.get(pk=templateid)
    except Emailtemplate.DoesNotExist:
        raise Http404("Template does not exist")
   # if request.method == 'POST':
    #    form = YourForm(request.POST)
     #   if form.is_valid():
      #      answer = form.cleaned_data['value']
       #     return render(request, 'civic/send.html', {
        #    'templates_all': Emailtemplate.objects.all(),
         #   'chosentemplate' : request.GET ,
          #  })
    #else:
    currenttemplateid = templateid
    selectedtemplatecontent = ''
    link = ''
    templateobject = None
    emails = '' # no email selected 
    if(templateid is not None):
        templateobject = Emailtemplate.objects.get(id = templateid)
        selectedtemplatecontent = templateobject.contentTemp
        link = 'mailto:' + emails + '?cc=&subject=' + urllib.parse.quote(templateobject.subject) + '&body=' + urllib.parse.quote(selectedtemplatecontent)
    if len(request.GET) > 0:
        selectedtemplateid = '' #placeholder code
    return render(request, 'civic/send.html', {
        'reps_all': me.representatives.all(),
        'chosentemplate' : selectedtemplatecontent ,
        'generatedlink' : link,
        'chosenrep' : '',
        'templateidvar' : currenttemplateid,
        'linkornot' : linkornot,
    })

def usetemplatenoid(request):
    if not request.user.is_authenticated:
        return render(request, 'civic/send.html', {
        'noclient': True,
    })
    me = client.objects.get(user = request.user)
    linkornot = 1
    selectedtemplatecontent = ''
    link = ''
    if request.method == 'GET' and 'repdropdown' in request.GET and 'htmlid' in request.GET:
        linkornot = 0
        templateobject = Emailtemplate.objects.get(id = request.GET.get('htmlid'))
        selectedtemplatecontent = templateobject.contentTemp
        link = 'mailto:' + request.GET.get('repdropdown') + '?cc=&subject=' + urllib.parse.quote(templateobject.subject) + '&body=' + urllib.parse.quote(selectedtemplatecontent)  
    return render(request, 'civic/send.html', {
        'reps_all': me.representatives.all(),
        'chosentemplate' : selectedtemplatecontent ,
        'chosenrep' : request.GET.get('repdropdown'),
        'generatedlink' : link,
        'templateidvar' : request.GET.get('htmlid'),
        'linkornot' : linkornot,
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

def logout_request(request):
    logout(request)
    return redirect("home")

def gauth(request):
    useremail = ''
    if request.user.is_authenticated:
        useremail = request.user.email
        if(User.objects.filter(email = useremail).count() == 0):
            userobj = User(name=request.user.username, email=useremail)
    return render(request, "gauth/index.html", {
        'useremail': useremail,
    })

@login_required
@transaction.atomic
def update_profile(request):
    me = client.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.clients)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect('/')
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.clients)
    status = 0
    errormessage = ""
    reps = ['','','','','']
    if len(request.GET) > 0:
        apireturn = request.GET['InputAddress']
        spaceremoved = apireturn.replace(' ', '+')
        response = requests.get('https://www.googleapis.com/civicinfo/v2/representatives?address=' + spaceremoved + '&key=AIzaSyBtQhDMbQxM85h35k2CNEzGpZpCY3o4eDs&levels=country', params=request.GET)
        apireturn = response.json()
        status = response.status_code
        if(status == 200):
            if len(apireturn['offices']) > 3:
                if 'cd:' in apireturn['offices'][3]['divisionId']:
                    locationhelp = apireturn['offices'][3]['divisionId']
                    me.State = locationhelp[locationhelp.find('state:') + 6:locationhelp.find('state:') + 8]
                    me.District = locationhelp[locationhelp.find('cd:') + 3:locationhelp.find('cd:') + 5]
                    me.save()
                    useremail = ''
                    if request.user.is_authenticated:
                        me.representatives.all().delete()
                        for i in range(5):
                            temp = apireturn['officials'][i]
                            reps[i] = temp['name']
                            if not Representative.objects.filter(name = temp['name']).exists():
                                repobj = Representative(name=temp['name'], party = temp['party'], email=re.sub("[^a-zA-Z]+", "", temp['name']) + '@us.gov')
                                if i > 1:
                                    repobj.state = me.State
                                else:
                                    repobj.state = ''
                                if i > 3:
                                    repobj.district = me.District
                                else:
                                    repobj.district = ''
                                repobj.save()
                            else:
                                repobj = Representative.objects.get(name = temp['name'])
                            me.representatives.add(repobj)
                            me.save()
                    else:
                        errormessage = 'the address is not specific enough, please enter a full address where you want to contact representatives (it does not need to be your address)'
            else:
                    errormessage = 'the address is not specific enough, please enter a full address where you want to contact representatives (it does not need to be your address)'
        else:
            errormessage = 'something is wrong with the address, please enter a full address where you want to contact representatives (it does not need to be your address)'
    return render(request, 'civic/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'apistatus' : errormessage,
        'me' : me,
        'allreps' : me.representatives.all(),
    })


def makeFavorite(request, templateid):
    try:
        if(templateid == 0 or not request.user.is_authenticated):
            currenttemplate = None
        else:
            currenttemplate = Emailtemplate.objects.get(pk=templateid)
    except Emailtemplate.DoesNotExist:
        raise Http404("Template does not exist")
    request.user.clients.favorites.add(currenttemplate)
    return HttpResponseRedirect('/'+str(templateid)+'/send')

def unFavorite(request, templateid):
    try:
        if(templateid == 0 or not request.user.is_authenticated):
            currenttemplate = None
        else:
            currenttemplate = Emailtemplate.objects.get(pk=templateid)
    except Emailtemplate.DoesNotExist:
        raise Http404("Template does not exist")
    request.user.clients.favorites.remove(currenttemplate)
    return HttpResponseRedirect('/select')
