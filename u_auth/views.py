from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

#################################################################################

def signin(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'login.html')

#################################################################################

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    return render(request,'index.html')

#################################################################################

@user_passes_test(lambda u: u.is_superuser)
def signout(request):
    logout(request)
    return redirect('sign-in')