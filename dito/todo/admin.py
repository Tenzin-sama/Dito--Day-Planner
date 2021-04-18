from django.contrib import admin
from .models import TodoCategory, TodoItem

# Register your models here.
admin.site.register(TodoCategory)
admin.site.register(TodoItem)