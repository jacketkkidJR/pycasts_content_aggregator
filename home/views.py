from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic import TemplateView
from datetime import datetime
from custom_user.models import User
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = 'password-reset-sent'


class UserCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class HomeView(TemplateView):
    template_name = 'homepage.html'
    extra_context = {'today': datetime.today()}


class SignupView(CreateView):
    form_class = UserCreation
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

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pycasts')
        return super().get(request, *args, **kwargs)