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
from signin.models import entries
from datetime import datetime



def signin(request):
    return render(request,'signin/signin.html',context={})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def lg_out(request):
    request.session.flush()
    request.user = AnonymousUser
    logout(request)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='')
def home(request,**kargs):
    user=request.user
    x=int(datetime.now().hour)
    greeting=" "
    # print(x)
    # if x<12 or x==24:
    #     greeting="Good Morning"
    # elif x>=12  and x<=16:
    #     greeting="Good Afternoon"
    # elif x>16 and x<20:
    #     greeting="Good Evening"
    # elif x>=20 and x<24:
    #     greeting="Good Night"
    if request.method=='POST':
        print(request.POST)
        if int(request.POST.get('rad'))==0:
            amount=-float(request.POST.get('amount'))
            cred_deb='Debit'
        elif int(request.POST.get('rad'))==1:
            amount=float(request.POST.get('amount'))
            cred_deb='Credit'
        record=entries(
            clientname = user.email,
            date= request.POST.get('date'),
            amount=amount,
            source_name=request.POST.get('source'),
            source_descip=request.POST.get('desc'),
            cred_deb= cred_deb
        )
        record.save()
    all_recs=entries.objects.filter(clientname=user.email)
    total_bal=0
    for rec in all_recs:
        total_bal=float(rec.amount)+ total_bal

    return render(request,'signin/index.html',{'greet':greeting,'all_recs':all_recs,'balance':total_bal})
