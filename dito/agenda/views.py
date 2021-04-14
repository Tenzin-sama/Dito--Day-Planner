from .forms import CreateAgendaForm, UpdateAgendaForm
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import Agenda
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class AgendaView(FormView, TemplateView, LoginRequiredMixin):
    model = Agenda
    template_name = "agenda/agenda_list.html"
    form_class = CreateAgendaForm

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)

        agendas = Agenda.objects.filter(user = self.request.user)
        context['agendas'] = agendas

        if 'create_agenda_form' not in context:
            context['create_agenda_form'] = CreateAgendaForm
        
        if 'update_agenda_form' not in context:
            context['update_agenda_form'] = UpdateAgendaForm
        
        return context
    
    def post(self, request, *args, **kwargs):

        context = {}

        if 'create_agenda' in request.POST:
            create_agenda_form = CreateAgendaForm(request.POST)

            if create_agenda_form.is_valid():
                create_agenda_form.save(self.request.user)
            else:
                context['create_agenda_form'] = create_agenda_form

        if 'update_agenda' in request.POST:
            update_agenda_form = UpdateAgendaForm(request.POST)
            if update_agenda_form.is_valid():
                agenda_pk = request.POST['agenda_pk']
                current_agenda = Agenda.objects.filter(pk = agenda_pk).first()
                update_agenda_form.save(self.request.user, current_agenda)
            else:
                context['update_agenda_form'] = update_agenda_form

        if 'remove_agenda' in request.POST:
            agenda_pk = request.POST['agenda_pk']
            current_agenda = Agenda.objects.filter(pk = agenda_pk).first()
            current_agenda.delete()

        return render(request, self.template_name, self.get_context_data(**context))