from .forms import CreateJournalForm, UpdateJournalForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from .models import Journal
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class JournalList(TemplateView, FormView, LoginRequiredMixin):
    model = Journal
    template_name = "journal/journal_list.html"
    form_class = CreateJournalForm

    def get_context_data(self, **kwargs):
        context = super(JournalList, self).get_context_data(**kwargs)

        journals = Journal.objects.filter(user = self.request.user)
        context['journals'] = journals

        if 'create_journal_form' not in context:
            context['create_journal_form'] = CreateJournalForm
        
        return context

    def post(self, request, *args, **kwargs):

        context = {}

        if 'create_journal' in request.POST:
            create_journal_form = CreateJournalForm(request.POST)
            print(create_journal_form.is_valid())
            if create_journal_form.is_valid():
                create_journal_form.save(self.request.user)
            else:
                context['create_journal_form'] = create_journal_form
        
        if 'remove_journal' in request.POST:
            journal_pk = request.POST['journal_pk']
            current_journal = Journal.objects.filter(pk = journal_pk).first()
            current_journal.delete()

        return render(request, self.template_name, self.get_context_data(**context))


class JournalDetail(TemplateView, FormView, LoginRequiredMixin):
    model = Journal
    template_name = "journal/journal_detail.html"
    form_class = CreateJournalForm

    def get_context_data(self, **kwargs):
        context = super(JournalDetail, self).get_context_data(**kwargs)

        journal = Journal.objects.filter(pk=self.kwargs['pk']).first()
        context['journal'] = journal

        if 'update_journal_form' not in context:
            context['update_journal_form'] = UpdateJournalForm

        return context

    def post(self, request, *args, **kwargs):

        context = {}
        current_journal = Journal.objects.filter(pk=self.kwargs['pk']).first()
        if 'update_journal' in request.POST:
            
            update_journal_form = UpdateJournalForm(request.POST)

            if update_journal_form.is_valid():
                update_journal_form.save(self.request.user, current_journal)
            else:
                context['update_journal_form'] = update_journal_form

        if 'remove_journal' in request.POST:
            current_journal.delete()
            return redirect('/journal')
        
        return render(request, self.template_name, self.get_context_data(**context))