from django.urls import path
from . import views
import string
import random
from django.urls import path,include
urlpatterns = [

path("",views.signin,name='signin'),
path('accounts/', include('allauth.urls')),
path('',views.lg_out,name='lg_out'),
# Dashboard URLS here
path("home",views.home,name='home'),

]
