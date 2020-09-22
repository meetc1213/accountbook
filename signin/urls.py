from django.urls import path
from . import views
import string
import random
from django.urls import path,include
urlpatterns = [
path('',views.home,name='home'),
path('',views.signin,name='signin'),
path('',views.gsignin,name='gsignin'),
path('password_reset/',views.password_reset,name='password_reset'),
path('signup/',views.signup,name='signup'),
path('accounts/', include('allauth.urls')),
path('',views.lg_out,name='lg_out'),
path(str(''.join(random.choices(string.ascii_uppercase+string.digits, k = 12)) ),views.code_verify,name='code_verify'),
]
