from django.shortcuts import render
from .models import Episode
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


class PodcastView(LoginRequiredMixin, ListView):
    model = Episode
    template_name = 'pycasts.html'
    login_url = '/login'
    def get_context_data(self, **kwargs):
        """Here we override the context data to show only 10 most recent podcasts"""
        context = super().get_context_data(**kwargs)
        context['episodes'] = Episode.objects.filter().order_by("-pub_date")[:10]
        return context


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = 'login'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pycasts')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'login.html'
    success_url = 'pycasts'