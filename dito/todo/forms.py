from django.forms import ModelForm
from django import forms
from .models import TodoCategory, TodoItem
from authentication.models import User

class CreateTodoCategoryForm(ModelForm):
    class Meta:
        fields=('name',)
        model = TodoCategory

    def save(self, user):
        todo_category = TodoCategory.objects.create(
            name = self.cleaned_data['name'],
            user = user,
        )
        return todo_category

class CreateTodoItemForm(ModelForm):
    class Meta:
        fields = ('text',)
        model = TodoItem
    
    def save(self, user, todo_category):
        todo_item = TodoItem.objects.create(
            text = self.cleaned_data['text'],
            category = todo_category,
        )
        return todo_item