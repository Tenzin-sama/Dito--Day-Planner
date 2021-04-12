from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls.base import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import ChangePasswordForm, UserForm
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User


def signUpView(request):
    if request.method == 'POST':
    

        user_form =UserForm(request.POST)

        if user_form.is_valid():
            # user = user_form.save(commit=False)
            user_form.save()

            return HttpResponseRedirect(reverse_lazy("authentication:login"))
        else:
            context={
                'user_form':user_form
            }

    else:
        context = {
            'user_form': UserForm(),
            
        }

    return render(request, 'authentication/signup.html', context)


# class ChangePasswordView(FormView, TemplateView, LoginRequiredMixin):
#     model = User
#     template_name = "authentication/change_password.html"
#     form_class = UserForm

#     def get_context_data(self, **kwargs):
#         print("aloha")
#         context = super(ChangePasswordView, self).get_context_data(**kwargs)

#         if 'change_password_form' in context:
#             context['change_password_form'] = ChangePasswordForm
#         return context
    
#     def post(self, request, *args, **kwargs):
#         context = {}
#         print("hi")
#         if 'change_password' in request.POST:
#             change_password_form = ChangePasswordForm(request.POST)
#             print("hello")
#             if change_password_form.is_valid():
#                 print("are you there?")
#                 change_password_form.save(self.request.user)
#             else:
#                 context['change_password_form'] = change_password_form
        
#         return render(request, self.template_name, **context)

# class ChangePasswordView(FormView, TemplateView, LoginRequiredMixin):
#     model = User
#     template_name = "authentication/change_password.html"
#     form_class = UserForm

#     def get_context_data(self, **kwargs):
#         context = super(ChangePasswordView, self).get_context_data(**kwargs)
#         print("aloha")
#         if 'change_password_form' not in context:
#             context['change_password_form'] = ChangePasswordForm

#         return context

#     def post(self, request, *args, **kwargs):
#         print("hi")
#         context = {}

#         if 'change_password' in request.POST:
#             change_password_form = ChangePasswordForm(request.POST)
#             print("hello")
#             if change_password_form.is_valid():
#                 print("are you there?")
#                 change_password_form.save(self.request.user)
#             else:
#                 context['change_password_form'] = change_password_form

#         return render(request, self.template_name, self.get_context_data(**context))


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication/change_password.html', {
        'form': form
    })