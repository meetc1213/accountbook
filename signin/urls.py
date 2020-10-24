from django.urls import path
from . import views
import string
import random
from django.urls import path,include
urlpatterns = [

path('',views.sign,name='sign'),
# path('signup/',views.signup,name='signup'),
path('accounts/', include('allauth.urls')),
path('',views.lg_out,name='lg_out'),
# Dashboard URLS here
path("home",views.home,name='home'),
path("create",views.create,name='create'),
path("join",views.join,name='join'),
path("manage",views.manage,name='manage'),
path("notifications",views.notifications,name='notifications'),
path("profile",views.profile,name='profile'),
# path(str(''.join(random.choices(string.ascii_uppercase+string.digits, k = 12)) ),views.code_verify,name='code_verify'),
]
