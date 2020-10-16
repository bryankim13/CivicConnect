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

class sendView(generic.TemplateView):
    template_name = 'civic/send.html'
    def get_context_data(self, **kwargs):
        context = {
        'templates_all': Emailtemplate.objects.all(),
        }
        return context