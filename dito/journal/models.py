from django.db import models
from ckeditor.fields import RichTextField
from authentication.models import User

# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=300)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="journal_user")