from django import forms
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms.forms import Form
from django.forms.models import ModelForm
from .models import User
from django.db.transaction import commit
import random
class UserForm(UserCreationForm):
   

    class Meta:
        model = User
        
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','user_type')


        @transaction.atomic()
        def save(self):
            user = User.objects.create(
                user_type=self.cleaned_data['user_type'],
                is_active = True
            )
            return user

class ChangePasswordForm(Form):
    old_password = forms.PasswordInput()
    new_password = forms.PasswordInput()

    def save(self, user):
        print(user.check_password(self.cleaned_data['old_password']))
        if user.check_password(self.cleaned_data['old_password']):
            user.set_password(self.cleaned_data['new_password'])
            user.save()
        return user