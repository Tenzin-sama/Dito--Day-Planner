from django.db import models
from authentication.models import User

# Create your models here.
class TodoCategory(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todo_user")

class TodoItem(models.Model):
    text = models.CharField(max_length=400)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(TodoCategory, on_delete=models.CASCADE, related_name="todo_category")