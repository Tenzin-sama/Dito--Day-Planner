from django.conf.urls import url
from django.urls import path
from . import views

app_name="todo"

urlpatterns=[
    path('', views.TodoView.as_view() ,name='todo_list'),
]