from django.urls import path

from . import views

urlpatterns = [
    path('pycasts', views.PodcastView.as_view(), name='pycasts'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]
