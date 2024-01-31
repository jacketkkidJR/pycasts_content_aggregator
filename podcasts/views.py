from django.shortcuts import render
from .models import Episode
from django.views.generic import ListView


class HomeView(ListView):
    model = Episode
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        """Here we override the context data to show only 10 most recent podcasts"""
        context = super().get_context_data(**kwargs)
        context['episodes'] = Episode.objects.filter().order_by("-pub_date")[:10]
        return context
