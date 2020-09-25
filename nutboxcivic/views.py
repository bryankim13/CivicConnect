from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView



def index(request):
    return HttpResponse("insert a complete Civic Connect project here -> 001")

class homeView(generic.TemplateView):
    template_name = 'civic/home.html'