from django.db import models
from authentication.models import User

# Create your models here.
class Agenda(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="agenda_user")
    color = models.CharField(max_length=30)