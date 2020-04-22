from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'signin/login.html',context={})
def signup(request):
    return render(request,'signin/signup.html',context={})
def password_reset(request):
    return render(request,'signin/fpwd.html',context={})
