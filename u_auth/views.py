from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from administrator.models import Category,Product,Lead,Lead_Update,Lead_Schedule,Attachments,Proposal
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
    total_leads = Lead.objects.filter(Status=1).count()
    Lead_Faild = Lead.objects.filter(Status=3,Lead_Status=0).count()
    Lead_Succes = total_leads - Lead_Faild

    total_opportunities = Lead_Succes
    Opportunity_Faild = Lead.objects.filter(Status=3,Lead_Status=1).count()
    Opportunity_Success = total_opportunities - Opportunity_Faild

    total_proposals = Proposal.objects.all().count()
    Proposal_Success = Proposal.objects.filter(Proposal_Status = 1).count()
    Proposal_Faild = Proposal.objects.filter(Proposal_Status = 0).count()
    Proposal_Pending = Proposal.objects.filter(Proposal_Status = 10).count()

    total_clients = Lead.objects.filter(Lead_Status=3,Status=1).count()
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
        'proposal_pending' : Proposal_Pending
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