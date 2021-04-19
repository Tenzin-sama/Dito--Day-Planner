from django.conf.urls import url
from django.urls import path
from . import views

app_name="admins"

urlpatterns=[
    path('', views.AdminDashboard.as_view() ,name='admin_dashboard'),
]