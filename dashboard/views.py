from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from signin.models import profile
from django.contrib import auth
from django.core.mail import send_mass_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime
import os
import psycopg2
# Create your views here.
DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def home(request,**kargs):
    user=request.user
    x=int(datetime.now().hour)
    greeting=" "
    if x<12 or x==24:
        greeting="Good Morning"
    elif x>12 and x<16:
        greeting="Good Afternoon"
    elif x>16 and x<20:
        greeting="Good Evening"
    elif x>=20 and x<24:
        greeting="Good Night"
    return render(request,'dashboard/home.html',{'fname':user.first_name,'h_active':'active','greet':greeting})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def create(request,**kwargs):
    return render(request,'dashboard/create.html',{'c_active':'active','bold':'bold'})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def join(request,**kwargs):
    return render(request,'dashboard/join.html',{'j_active':'active','bold':'bold'})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def manage(request,**kwargs):
    return render(request,'dashboard/manage.html',{'m_active':'active','bold':'bold'})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def notifications(request,**kwargs):
    return render(request,'dashboard/notifications.html',{'n_active':'active','bold':'bold'})

def profile(request,**kwargs):
    return render(request,'dashboard/profile.html',{'bold':'bold'})
