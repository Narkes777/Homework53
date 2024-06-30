from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Human
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
# Create your views here.


class HumanList(LoginRequiredMixin, ListView):

    model = Human
    template_name = 'app/human_list.html'
    context_object_name = 'people'
    paginate_by = 3
    paginate_orphans = 1



class HumanDetail(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Human
    template_name = 'app/human_detail.html'
    context_object_name = 'human'




class UserRegisterView(FormView):
    template_name = 'app/registration.html'
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        pass1 = data.pop('password1') # None
        pass2 = data.pop('password2') # None
        form = UserRegistrationForm(request.POST)
        if pass1 != pass2:
            return self.form_invalid(form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponse('New user has been created')



class UserLoginView(LoginView):
    template_name = 'app/login.html'