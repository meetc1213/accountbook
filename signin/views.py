from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.mail import send_mail
from django.conf import settings
from random import randint
import re
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from signin.models import clubs
# from datetime import datetime
# from urllib import urlencode
# from django.conf import settings
# from django.contrib import messages
# from app.models import User
# Create your views here.

Name=""
Class=""
Email=""
Password=""
code=0
fcode=0
sent=False
registered=False
verified=False
pwd_change=False
pwd_change_user=""

@cache_control(no_cache=True, must_revalidate=True)
@csrf_protect
def sign(request):
    message={'cred_err':False}
    from django.apps import apps

    if request.user.is_authenticated:
        print("HoUSTON, WE HAVE A PROBLEM")

    if request.method=='POST':
        if len(request.POST)==4:
            user =authenticate(username=request.POST.get('email'),password=request.POST.get('pwd'))
            if user:
                login(request, user)
                return redirect('home')
            else:
                print("incofffffffffff")
                message['cred_err']=True

        # Sign up form here.
        elif len(request.POST)==5:
            # collecting details
            Name=request.POST.get('name')
            Email=request.POST.get('email')
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request,'signin/index.html',context={'exist':True})
            except:
                import random, string
                code=str(''.join(random.choices(string.ascii_uppercase+string.digits, k = 12)) )
                send_mail(
                    'Sign Up on JPIS Clubs',
                    "Hello "+Name+"\n\nThank you for taking the first step. Your password for JPIS Clubs is "+str(code),
                    settings.EMAIL_HOST_USER,[request.POST.get('email')]
                    )
                user = User.objects.create_user( username=Email,
                first_name=Name, password=str(code))
                user.set_password(str(code))
                user.is_active = True
                user.save()
                return render(request,'signin/index.html',context={'sent':True})

    return render(request,'signin/index.html',context=message)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def lg_out(request):
    request.session.flush()
    request.user = AnonymousUser
    logout(request)


# Dashboard views here
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
# from signin.models import profile
from django.contrib import auth
from django.core.mail import send_mass_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from datetime import datetime

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def home(request,**kargs):
    user=request.user
    x=int(datetime.now().hour)
    greeting=" "
    print(x)
    if x<12 or x==24:
        greeting="Good Morning"
    elif x>=12  and x<=16:
        greeting="Good Afternoon"
    elif x>16 and x<20:
        greeting="Good Evening"
    elif x>=20 and x<24:
        greeting="Good Night"
    return render(request,'dashboard/home.html',{'fname':user.first_name,'h_active':'active','greet':greeting})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def create(request,**kwargs):
    if request.method =='POST':
        club=clubs(clubimage=request.FILES['logo'],
        clubname=request.POST.get('club_name'),
        clubtagline=request.POST.get('club_moto'),
        clubdesc=request.POST.get('club_descrip'),
        memsize=request.POST.get('mem_size'),
        nofevents=request.POST.get('meet_no'),
        president=request.user.first_name,
        contact_mail=request.user.username,
        )
        club.save()
        return redirect('join')
    return render(request,'dashboard/create.html',{'c_active':'active','bold':'bold'})
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')

def join(request,**kwargs):
    all_clubs = clubs.objects.all()
    print(all_clubs)
    return render(request,'dashboard/join.html',{'j_active':'active','bold':'bold','clubs':all_clubs})
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
