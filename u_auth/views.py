from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from administrator.models import Category,Product,Lead,Lead_Update,Lead_Schedule,Attachments,Proposal,Sales_Target,User
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

    d = date.today()
    year = d.year

    total_leads = Lead.objects.filter(Status=1).count()
    Lead_Faild = Lead.objects.filter(Status=3,Lead_Status=0).count()
    Lead_Succes = total_leads - Lead_Faild

    total_opportunities = Lead_Succes
    Opportunity_Faild = Lead.objects.filter(Status=3,Lead_Status=1).count()
    Opportunity_Success = total_opportunities - Opportunity_Faild

    total_proposals = Proposal.objects.all()
    Proposal_Success = Proposal.objects.filter(Proposal_Status = 1)
    Proposal_Faild = Proposal.objects.filter(Proposal_Status = 0)
    Proposal_Pending = Proposal.objects.filter(Proposal_Status = 10)

    total_clients = Lead.objects.filter(Lead_Status=3,Status=1).count()
    meetings_today = Lead_Schedule.objects.filter(AddedDate=date.today()).count()

    salesmans = Sales_Target.objects.filter(From__year = year)

    targets = Sales_Target.objects.all()

    proposal_success_volume = 0
    proposal_failed_volume = 0
    proposal_pending_volume = 0

    full_archived = 0
    half_archived = 0
    morethan_half_archived = 0

    for p in total_proposals:
        if p.Proposal_Status == 1:
            proposal_success_volume += p.Grand_Total
        elif p.Proposal_Status == 0:
            proposal_failed_volume += p.Grand_Total
        elif p.Proposal_Status == 10:
            proposal_pending_volume += p.Grand_Total

    
    for s in salesmans:
        t = s.Archived / s.Targets 
        if t >= 1 :
            full_archived += 1
        elif t > 0.5:
            morethan_half_archived += 1
        elif t == 0.5:
            half_archived += 1

    
    yrs = []

    reports = []

    for target in targets:
        yrs.append(target.From.year)
    years = [*set(yrs)]
    
    for year in years:
        archived = 0
        ts = Sales_Target.objects.filter(From__year = year)
        for t in ts:
            archived += t.Archived
        report = {'year':year,'archived':archived}
        reports.append(report)

    context = {
        'total_leads' : total_leads,
        'total_opportunities' : total_opportunities,
        'total_proposals' : total_proposals.count(),
        'total_clients' : total_clients,
        'meetings_today' : meetings_today,
        'lead_success' : Lead_Succes,
        'lead_faild' : Lead_Faild,
        'opportunity_success' : Opportunity_Success,
        'opportunity_failed' : Opportunity_Faild,
        'proposal_success' : Proposal_Success.count(),
        'proposal_failed' : Proposal_Faild.count(),
        'proposal_pending' : Proposal_Pending.count(),
        'psv' : proposal_success_volume,
        'ppv' : proposal_pending_volume,
        'pfv' : proposal_failed_volume,
        'fa' : full_archived,
        'hf' : half_archived,
        'mhf' : morethan_half_archived,
        'reports':reports
    }

    return render(request,'index.html',context)

#################################################################################

@login_required
def salesboard(request):
    return render(request,'salesboard.html')

#################################################################################

def changepassword(request):
    user = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.warning(request,'password does not matching')
            return redirect('.')
        else:
            user.set_password(password1)
            user.save()
            return redirect('dashboard')
    return render(request,'change-password.html')

#################################################################################

@user_passes_test(lambda u: u.is_superuser)
def signout(request):
    logout(request)
    return redirect('sign-in')