from django.shortcuts import render
from .models import Episode
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class PodcastView(LoginRequiredMixin, ListView):
    model = Episode
    template_name = 'pycasts.html'
    login_url = '/login'
    def get_context_data(self, **kwargs):
        """Here we override the context data to show only 10 most recent podcasts"""
        context = super().get_context_data(**kwargs)
        context['episodes'] = Episode.objects.filter().order_by("-pub_date")[:10]
        return context


