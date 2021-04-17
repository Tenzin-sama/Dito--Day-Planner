from django.conf.urls import url
from django.urls import path
from . import views

app_name="journal"

urlpatterns=[
    path('', views.JournalList.as_view() ,name='journal_list'),
    path('<int:pk>/', views.JournalDetail.as_view(), name='journal_detail')
]