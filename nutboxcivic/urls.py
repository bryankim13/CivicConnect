"""nutboxcivic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from nutboxcivic import views
from .views import homeView

urlpatterns = [
    path('', homeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('send/', views.usetemplatenoid, name = 'send'),
    path('<templateid>/send/', views.usetemplate, name = 'send'),
    path('select/', views.selecttemplate, name = "select"),
    path('createTemplate', views.formTemplate.as_view(), name = 'createTemp'),
    path('creatingTemplate', views.formingTemp, name = 'creatingTemp'),
    path('thanksforsubmitting', views.thanksView.as_view(), name = 'thanksSubmit'),
    path('profile/', views.update_profile, name = 'profile'),
    path('gauth', views.gauth, name = 'gauth'),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls'), name = 'user'),
    path("logout/", views.logout_request, name="logout"),

]
