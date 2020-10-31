from django.contrib import admin

from .models import Emailtemplate, Issue, Representative

admin.site.register(Emailtemplate)
admin.site.register(Issue)
admin.site.register(Representative)
