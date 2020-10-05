from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class userindexView(generic.TemplateView):
    template_name = 'user/userindex.html'