from django.db import models
from django.contrib.auth.models import AbstractUser
import random


# Create your models here.
class User(AbstractUser):

    
    # Boolean Fields for determining user types
    USER_CHOICES=(
        (1,"Admin"),
        (2,"Personal")
    )



    user_type=models.PositiveIntegerField(choices=USER_CHOICES,default=2)

    # user_color= models.CharField(max_length=20,default="%06x" % random.randint(0, 0xFFFFFF))

    # String representation of the User model
    def __str__(self):
        return self.username