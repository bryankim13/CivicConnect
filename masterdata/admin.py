from django.contrib import admin

from .models import Emailtemplate, Representative, Issue

admin.site.register(Emailtemplate)
admin.site.register(Representative)
admin.site.register(Issue)