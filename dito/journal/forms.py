from django.forms import ModelForm, fields
from django import forms
from .models import Journal
from ckeditor.widgets import CKEditorWidget

class CreateJournalForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Journal
        fields = ('title',)
    
    def save(self, user):
        journal = Journal.objects.create(
            title = self.cleaned_data['title'],
            content = self.cleaned_data['content'],
            user = user,
        )
        return journal


class UpdateJournalForm(ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Journal
        fields = ('title',)
    
    def save(self, user, journal):
        if journal.user == user:
            journal.title = self.cleaned_data['title']
            journal.content = self.cleaned_data['content']
            journal.save()
        return journal