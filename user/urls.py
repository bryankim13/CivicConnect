from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.userindexView.as_view(), name='userindex'),
]
