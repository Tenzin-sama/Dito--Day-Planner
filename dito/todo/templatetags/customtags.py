from django import template
from todo.models import TodoItem

register = template.Library()

# def order_category(item, category):
#     if item.category == category:
#         return True
#     else:
#         return False