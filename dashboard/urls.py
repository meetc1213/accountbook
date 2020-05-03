from django.urls import path
from . import views

urlpatterns = [
path("home",views.home,name='home'),
path("create",views.create,name='create'),
path("join",views.join,name='join'),
path("manage",views.manage,name='manage'),
path("notifications",views.notifications,name='notifications'),
path("profile",views.profile,name='profile'),
]