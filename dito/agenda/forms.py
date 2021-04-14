from django.forms import ModelForm
from django import forms
from .models import Agenda
import datetime

class CreateAgendaForm(ModelForm):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    class Meta:
        fields=('title', 'description', 'date', 'color')
        model = Agenda

    def save(self, user):
        agenda = Agenda.objects.create(
            title = self.cleaned_data['title'],
            description = self.cleaned_data['description'],
            date = self.cleaned_data['date'],
            color = self.cleaned_data['color'],
            user = user,
        )
        return agenda

class UpdateAgendaForm(ModelForm):
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker2'
    #     })
    # )
    class Meta:
        fields=('title', 'description', 'color')
        model = Agenda      

    def save(self, user, agenda):
        if agenda.user == user:
            agenda.title = self.cleaned_data['title']
            agenda.description = self.cleaned_data['description']
            # agenda.date = date
            print(self.cleaned_data['color'])
            agenda.color = self.cleaned_data['color']
            agenda.save()
        return agenda