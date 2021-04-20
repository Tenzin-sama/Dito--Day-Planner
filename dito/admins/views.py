from authentication.forms import UserForm
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentication.models import User

# Create your views here.
class AdminDashboard(FormView, TemplateView, LoginRequiredMixin):
    model = User
    template_name = "admins/dashboard.html"
    form_class = UserForm

    def get_context_data(self, **kwargs):
        context = super(AdminDashboard, self).get_context_data(**kwargs)

        user_count = User.objects.filter(user_type=2).count()
        users = User.objects.all()

        context['user_count'] = user_count
        context['users'] = users

        return context

    def post(self, request, *args, **kwargs):

        context = {}

        if 'suspend_user' in request.POST:
            user_object_pk = request.POST['user_object_pk']
            selected_user = User.objects.filter(pk= user_object_pk).first()
            selected_user.is_active = False
            selected_user.save()
            print(selected_user.is_active)
        
        if 'reactivate_user' in request.POST:
            user_object_pk = request.POST['user_object_pk']
            selected_user = User.objects.filter(pk= user_object_pk).first()
            selected_user.is_active = True
            selected_user.save()
            print(selected_user.is_active)

        if 'delete_user' in request.POST:
            user_object_pk = request.POST['user_object_pk']
            selected_user = User.objects.filter(pk= user_object_pk).first()
            selected_user.delete()

        return render(request, self.template_name, self.get_context_data(**context))