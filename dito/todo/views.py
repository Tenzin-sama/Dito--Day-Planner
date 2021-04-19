from .forms import CreateTodoCategoryForm, CreateTodoItemForm
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .models import TodoCategory, TodoItem
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class TodoView(FormView, TemplateView, LoginRequiredMixin):
    model = TodoCategory
    template_name = "todo/todo_list.html"
    form_class = CreateTodoCategoryForm

    def get_context_data(self, **kwargs):
        context = super(TodoView, self).get_context_data(**kwargs)

        todo_categories = TodoCategory.objects.filter(user = self.request.user)
        todo_items = TodoItem.objects.filter(category__user = self.request.user)
        context['todo_categories'] = todo_categories
        context['todo_items'] = todo_items

        if 'create_category_form' not in context:
            context['create_category_form'] = CreateTodoCategoryForm

        if 'create_todo_form' not in context:
            context['create_todo_form'] = CreateTodoItemForm

        return context

    def post(self, request, *args, **kwargs):

        context = {}

        if 'create_category' in request.POST:
            create_category_form = CreateTodoCategoryForm(request.POST)

            if create_category_form.is_valid():
                create_category_form.save(self.request.user)
            else:
                context['create_category_form'] = create_category_form
        
        if 'delete_category' in request.POST:
            category_pk = request.POST['category_pk']
            current_category = TodoCategory.objects.filter(pk=category_pk).first() # put some logic here
            current_category.delete()
        
        if 'create_item' in request.POST:
            create_todo_form = CreateTodoItemForm(request.POST)
            current_category = TodoCategory.objects.filter(pk=request.POST['item_category']).first()
            if create_todo_form.is_valid():
                create_todo_form.save(self.request.user, current_category) # find second argument logic
            else:
                context['create_todo_form'] = CreateTodoItemForm

        if 'remove_item' in request.POST:
            item_pk = request.POST['item_pk']
            current_item = TodoItem.objects.filter(pk = item_pk).first() # put some logic here
            current_item.delete()
        
        if 'uncheck_item' in request.POST:
            item_pk = request.POST['item_pk']
            current_item = TodoItem.objects.filter(pk = item_pk).first() # put some logic here
            current_item.completed = False
            current_item.save()
        
        if 'check_item' in request.POST:
            item_pk = request.POST['item_pk']
            current_item = TodoItem.objects.filter(pk = item_pk).first() # put some logic here
            current_item.completed = True
            current_item.save()

        
        return render(request, self.template_name, self.get_context_data(**context))
    
