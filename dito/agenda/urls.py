from django.conf.urls import url
from django.urls import path
from . import views

app_name="agenda"

urlpatterns=[
    path('', views.AgendaView.as_view() ,name='agenda_list'),
]