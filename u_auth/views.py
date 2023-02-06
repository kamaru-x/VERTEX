from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from administrator.models import Category,Product,Lead,Lead_Update,Lead_Schedule,Attachments
from datetime import date

# Create your views here.

#################################################################################

def signin(request):
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect('dashboard')
            elif request.user.is_salesman:
                return redirect('salesboard')
        else:
            messages.error(request,'incorrect username or password')
            return redirect('.')
    return render(request,'login.html')

#################################################################################

@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    total_leads = Lead.objects.all().count()
    Lead_Faild = Lead.objects.filter(Status=3).filter(Lead_Status=1).count()
    Lead_Succes = total_leads - Lead_Faild

    total_opportunities = Lead.objects.filter(Lead_Status=2).filter(Status=1).count()
    Opportunity_Success = Lead.objects.filter(Lead_Status=3).filter(Status=1).count()
    Opportunity_Faild = Lead.objects.filter(Lead_Status=2).filter(Status=3).count()

    total_proposals = Lead.objects.filter(Lead_Status=2).filter(Status=1).count()
    Proposal_Success = Lead.objects.filter(Lead_Status=3).count()
    Proposal_Faild = Lead.objects.filter(Lead_Status=3).filter(Status=3).count()

    total_clients = Lead.objects.filter(Lead_Status=3).filter(Status=1).count()
    meetings_today = Lead_Schedule.objects.filter(AddedDate=date.today()).count()

    context = {
        'total_leads' : total_leads,
        'total_opportunities' : total_opportunities,
        'total_proposals' : total_proposals,
        'total_clients' : total_clients,
        'meetings_today' : meetings_today,
        'lead_success' : Lead_Succes,
        'lead_faild' : Lead_Faild,
        'opportunity_success' : Opportunity_Success,
        'opportunity_failed' : Opportunity_Faild,
        'proposal_success' : Proposal_Success,
        'proposal_failed' : Proposal_Faild,
    }

    return render(request,'index.html',context)

#################################################################################

@login_required
def salesboard(request):
    return render(request,'salesboard.html')

#################################################################################

@user_passes_test(lambda u: u.is_superuser)
def signout(request):
    logout(request)
    return redirect('sign-in')