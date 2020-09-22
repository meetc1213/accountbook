from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from signin.models import profile
from django.contrib import auth
from django.core.mail import send_mass_mail
from django.conf import settings
from random import randint
import re
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout

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
def gsignin(request):
    return 1    

#     redirect_uri = "%s://%s%s" % (
#         request.scheme, request.get_host(), reverse('pain:google_login')
#     )
#     if('code' in request.GET):
#         params = {
#             'grant_type': 'authorization_code',
#             'code': request.GET.get('code'),
#             'redirect_uri': redirect_uri,
#             'client_id': settings.GP_CLIENT_ID,
#             'client_secret': settings.GP_CLIENT_SECRET
#         }
#         url = 'https://accounts.google.com/o/oauth2/token'
#         response = requests.post(url, data=params)
#         url = 'https://www.googleapis.com/oauth2/v1/userinfo'
#         access_token = response.json().get('access_token')
#         response = requests.get(url, params={'access_token': access_token})
#         user_data = response.json()
#         email = user_data.get('email')
#         if email:
#             user, _ = User.objects.get_or_create(email=email, username=email)
#             gender = user_data.get('gender', '').lower()
#             if gender == 'male':
#                 gender = 'M'
#             elif gender == 'female':
#                 gender = 'F'
#             else:
#                 gender = 'O'
#             data = {
#                 'first_name': user_data.get('name', '').split()[0],
#                 'last_name': user_data.get('family_name'),
#                 'google_avatar': user_data.get('picture'),
#                 'gender': gender,
#                 'is_active': True
#             }
#             user.__dict__.update(data)
#             user.save()
#             user.backend = settings.AUTHENTICATION_BACKENDS[0]
#             login(request, user)
#         else:
#             messages.error(
#                 request,
#                 'Unable to login with Gmail Please try again'
#             )
#         return redirect('/')
#     else:
#         url = "https://accounts.google.com/o/oauth2/auth?client_id=%s&response_type=code&scope=%s&redirect_uri=%s&state=google"
#         scope = [
#             "https://www.googleapis.com/auth/userinfo.profile",
#             "https://www.googleapis.com/auth/userinfo.email"
#         ]
#         scope = " ".join(scope)
#         url = url % (settings.GP_CLIENT_ID, scope, redirect_uri)
#         return redirect(url)











def home(request):
     return render(request,'signin/index.html',context={})
@cache_control(no_cache=True, must_revalidate=True)
@csrf_protect
def signin(request):
    global registered
    message={'registered':registered,'pwd_change':pwd_change}
    from django.apps import apps

    if request.user.is_authenticated:
        print("HoUSTON, WE HAVE A PROBLEM")

    if request.method=='POST':
        user =authenticate(username=request.POST.get('email'),password=request.POST.get('pwd'))
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            message['cred_err']=True

    return render(request,'signin/signin.html',context=message)
@csrf_protect
def password_reset(request):
    if request.method=='POST':
        print("INSIDE POST")
        global sent
        global fcode
        global pwd_change_user
        if sent==False:
            try:
                user = User.objects.get(username=request.POST['email'])
                fcode=randint(100000,999999)
                mail=('Reset Password',"Hello "+user.first_name+" "+user.last_name+",\n\nForgot your password? No worries. Use this 6-digit code "+str(fcode)+" for resetting your password.",settings.EMAIL_HOST_USER,request.POST['email'])
                send_mass_mail((mail,),fail_silently=False,)
                sent=True
                pwd_change_user=user
                return render(request,'signin/fpwd.html',context={'err':False,'sent':True,'verified':False,'email':user})
            except:
                return render(request,'signin/fpwd.html',context={'err':True,'sent':False})

        else:
            global verified
            if verified==False:
                if str(fcode)==request.POST['rcode']:
                    verified=True
                    return render(request,'signin/fpwd.html',
                    context={'err':False,'sent':True,'verified':True})
                else:
                    return render(request,'signin/fpwd.html',
                    context={'err':False,'sent':True,'verified':False,'verr':True})
            else:
                if request.POST['npwd']==request.POST['cnpwd']:
                    global pwd_change
                    pwd_change=True
                    u = User.objects.get(username=pwd_change_user.username)
                    u.set_password(request.POST['npwd'])
                    u.save()
                    sent = False
                    return redirect('signin')
                else:
                    return render(request,'signin/fpwd.html',
                    context={'err':False,'sent':True,'verified':True,'dpwderr':True})
    print("Not posted yet")
    return render(request,'signin/fpwd.html',context={'sent':False})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def lg_out(request):
    request.session.flush()
    request.user = AnonymousUser
    logout(request)
def signup(request):

    if request.method=='POST':
        global Class
        global Email
        global Password
        global Name
        Name=request.POST['name'].split()
        Class=request.POST['grade']+"-"+request.POST['section']
        Email=request.POST['email']
        Password=request.POST['pwd']
        error_dict={'name_err':"",'Name':Name,
        'grade':request.POST['grade'],'section':request.POST['section'],
        'Email':Email,'Password':Password}
        if len(re.findall(r'\w+', request.POST['name']))==1:
            error_dict['name_err']=True
            error_dict['Name']=Name[0]
            error_dict['errors']=True
            return render(request,'signin/signup.html',
            context=error_dict)
        try:
            user = User.objects.get(username=request.POST['email'])
            return render(request,'signin/signup.html',context={'err':True})
        except:
            # Sending verification email
            global code
            code=randint(100000,999999)
            mail=('Email Verification',"Hello "+Name[0]+" "+Name[1],"\n\nThank you for taking the first step. Your 6-digit code for email verification is "+str(code),settings.EMAIL_HOST_USER,[Email])
            send_mass_mail((mail,),fail_silently=False,)
            return redirect('code_verify')
    return render(request,'signin/signup.html',context={'errors':False})

def code_verify(request):
    values={}
    global v_msg
    global Class
    global Email
    global Password
    global Name
    global registered
    if request.method=='POST':

        if request.POST['vcode']==str(code):
            print("VERIFYIED")
            user = User.objects.create_user( username=Email,
            first_name=Name[0],last_name=Name[1],email=Email, password=Password)
            user.set_password(Password)
            user.is_active = True
            user.save()
            profile1=profile()
            profile1.user=user
            profile1.Class=Class
            profile1.save()
            print("user SAVED")
            registered=True
            print("FUCK IT")
            return redirect('signin')
        else:
            values['err']=True
            values['invalid']="The code is incorrect"
            values['email']=Email

    return render(request,'signin/email_verification.html',context=values)
