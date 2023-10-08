from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import login

# Create your views here.
class LoginPage(LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'

class Logout(LoginRequiredMixin, LogoutView):
    next_page = 'login'

class RegisterView(FormView):
    redirect_authenticated_user = True
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)