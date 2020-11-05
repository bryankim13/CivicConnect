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


import urllib #to encode email templates into url format for the mailto url link
#urllib.unquote(selectedtemplatecontent.value).decode('utf8')


class homeView(generic.TemplateView):
    template_name = 'civic/home.html'

class formTemplate(generic.CreateView):
    form_class = templateForm
    model = Emailtemplate
    template_name = 'civic/createTemp.html'

class thanksView(generic.TemplateView):
    template_name = 'civic/thankyou.html'

def formingTemp(request):
    if request.method == "POST":
        form = templateForm(request.POST)
        if form.is_valid():
            emTemp = form.save(commit=False)
            emTemp.save()
    return HttpResponseRedirect(reverse('thanksSubmit'))


def usetemplate(request, templateid):
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
    selectedtemplatecontent = ''
    link = ''
    templateobject = None
    emails = 'leyew99290@ofdyn.com' # a temporary email 
    if(templateid is not None):
        templateobject = Emailtemplate.objects.get(id = templateid)
        selectedtemplatecontent = templateobject.contentTemp
        link = 'mailto:' + emails + '?cc=&subject=' + urllib.parse.quote(templateobject.subject) + '&body=' + urllib.parse.quote(selectedtemplatecontent)
    if len(request.GET) > 0:
        selectedtemplateid = '' #placeholder code
    return render(request, 'civic/send.html', {
        'templates_all': Emailtemplate.objects.all(),
        'chosentemplate' : selectedtemplatecontent ,
        'generatedlink' : link,
    })

def usetemplatenoid(request):
    selectedtemplatecontent = ''
    link = ''
    emails = 'leyew99290@ofdyn.com' # a temporary email    
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
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.clients)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect('/')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.clients)
    return render(request, 'civic/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
