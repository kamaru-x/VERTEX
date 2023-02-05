from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Lead,Lead_Schedule,Lead_Update,Attachments,Product,Task,Proposal,Replays,Salesman_Report,Review
from u_auth.models import User
from datetime import date as dt
from administrator.views import setip

from administrator.views import setreport

# Create your views here.

@login_required
def list_opertunities(request):
    opertunities = Lead.objects.filter(Lead_Status=1).filter(Status=1)
    if request.method == 'POST':
        c = request.POST.get('c')
        lead= Lead.objects.get(id=c)
        lead.Status = 3
        lead.save()
        return redirect('list-opportunities')
    return render(request,'opportunity-list.html',{'opertunitunities':opertunities})

#################################################################################

@login_required
def view_opertunity(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    # attachments = Attachments.objects.all()

    if request.method == 'POST':
        if request.POST.get('date'):
            date = request.POST.get('date')
            description = request.POST.get('update-description')

            data = Lead_Update(Date=d,AddedBy=user,Ip=ip,Lead=lead,Description=description,AddedDate=date)
            data.save()

            ld = Lead_Update.objects.filter(Lead=lead).filter(AddedBy=user).last()
            attachment = request.FILES.getlist('attachment')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                ld.Attachments.add(attach)
                ld.save()

        if request.POST.get('sdate'):
            sdate = request.POST.get('sdate')
            mode = request.POST.get('mode')
            ftime = request.POST.get('from')
            to = request.POST.get('to')
            sdescription = request.POST.get('sdescription')

            data = Lead_Schedule(Date=d,AddedBy=user,Ip=ip,Lead=lead,Mode=mode,From=ftime,To=to,Description=sdescription,AddedDate=sdate)
            data.save()

        if request.POST.get('udate'):
            udate = request.POST.get('udate')
            udescription = request.POST.get('u-description')
            participends = request.POST.get('participents')
            id = request.POST.get('id')
            meeting = Lead_Schedule.objects.get(id=id)
            meeting.Update_Description = udescription
            meeting.Update_Date = udate
            meeting.Members = participends
            meeting.save()

            attachment = request.FILES.getlist('attach')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                meeting.Attachment.add(attach)
                meeting.save()

        return redirect('/opportunity-view/%s' %lead.id)

    schedules = Lead_Schedule.objects.filter(Lead=lead)

    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate >= dt.today() :
            upcoming.append(schedule)

    context = {
        'lead' : lead,
        'lead_update' : lead_update,
        # 'attachments' : attachments,
        'previous' : previous,
        'upcoming' : upcoming,
    }
    return render(request,'opportunity-view.html',context)

#################################################################################

@login_required
def create_proposal(request,lid):
    products = Product.objects.all()
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)

    try :
        proposal = Proposal.objects.get(Lead=lead)
    except :
        proposal = Proposal(Date=d,AddedBy=user,Ip=ip,Lead=lead)
        proposal.save()



    if request.method == 'POST':
        if request.POST.get('product'):
            product = request.POST.get('product')
            p = Product.objects.get(id=product)
            proposal.Products.add(p)
            proposal.save()
            return redirect('/proposal/%s' %lead.id)
        
        if request.POST.get('scope'):
            proposal.Scope = request.POST.get('scope')
            proposal.save()
            return redirect('/proposal/%s' %lead.id)

        if request.POST.get('payment'):
            proposal.Payment = request.POST.get('payment')
            proposal.save()
            return redirect('/proposal/%s' %lead.id)

        if request.POST.get('exclusion'):
            proposal.Exclusion = request.POST.get('exclusion')
            proposal.save()
            return redirect('/proposal/%s' %lead.id)

        if request.POST.get('terms'):
            proposal.Terms_Condition = request.POST.get('terms')
            proposal.save()
            return redirect('/proposal/%s' %lead.id)

        if request.POST.get('opportunity'):
            proposal.Oppertunity = request.POST.get('opportunity')
            proposal.save()
            return redirect('/proposal/%s' %lead.id)

    if proposal.Scope and proposal.Payment and proposal.Exclusion and proposal.Terms_Condition :
        proposal.Lead.Lead_Status = 2
        proposal.Lead.To_Client = d
        proposal.Lead.To_Proposal = d
        proposal.Lead.save()
        return redirect('clients')

    # pro = Proposal.objects.get(lead=lead)
    context = {
        'products' : products,
        # 'exclude' : exclude,
        'proposal' : proposal,
        # 'pro' : pro,
    }
    return render(request,'proposal.html',context)

#################################################################################

@login_required
def create_task(request):
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    leads = Lead.objects.all()
    if request.method == 'POST':
        lead = request.POST.get('lead')
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        description = request.POST.get('description')

        try:
            ld = Lead.objects.get(id=lead)
        except:
            return redirect('.')

        data = Task(Date=d,AddedBy=user,Ip=ip,Lead=ld,Title=title,Priority=priority,Due_Date=date,Description=description)
        data.save()

        ls = Task.objects.filter(Lead=ld).filter(AddedBy=user).last()
        attachment = request.FILES.getlist('attach')
        for a in attachment:
            if str(a).endswith(('.png', '.jpg', '.jpeg')):
                format = 'image'
            else:
                format = 'file'
            attach = Attachments(Attachment=a,Name=a,Format=format)
            attach.save()
            ls.Attachment.add(attach)
            ls.save()
        return redirect('pending-task')

    context = {
        'leads' : leads
    }
    return render(request,'create-task.html',context)

#################################################################################

@login_required
def pending_task(request):
    tasks = Task.objects.filter(Task_Status=0).filter(Status=1)
    user = request.user.id
    ip = setip(request)
    d = dt.today()
    if request.method == 'POST' :
        if request.POST.get('taskid'):
            tid = request.POST.get('taskid')
            task = Task.objects.get(id=tid)
            date = request.POST.get('date')
            description = request.POST.get('update-description')
            task.Task_Status = 1
            task.Completed_Date = d
            task.save()

            data = Review(Task=task,Message=description,AddedDate=date)
            data.save()

            ld = Review.objects.last()
            attachment = request.FILES.getlist('attachment')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                ld.Attachments.add(attach)
                ld.save()
            return redirect('pending-task')

        if request.POST.get('id'):
            id = request.POST.get('id')
            task = Task.objects.get(id=id)
            task.Status = 0
            task.save()
            return redirect('pending-task')        

    context = {
        'tasks' : tasks,
    }
    return render(request,'task-pending.html',context)

#################################################################################

@login_required
def completed_task(request):
    tasks = Task.objects.filter(Task_Status=1)
    return render(request,'task-completed.html',{'tasks':tasks})

#################################################################################

@login_required
def edit_task(request,tid):
    task = Task.objects.get(id=tid)
    leads = Lead.objects.all()
    user = request.user.id
    if request.method == 'POST':
        lead = request.POST.get('lead')
        ld = Lead.objects.get(id=lead)

        task.Lead = ld
        task.Title = request.POST.get('title')
        task.Priority = request.POST.get('priority')
        task.Due_Date = request.POST.get('date')
        task.Description = request.POST.get('description')
        task.save()

        ls = Task.objects.filter(Lead=ld).filter(AddedBy=user).last()
        attachment = request.FILES.getlist('attach')
        for a in attachment:
            if str(a).endswith(('.png', '.jpg', '.jpeg')):
                format = 'image'
            else:
                format = 'file'
            attach = Attachments(Attachment=a,Name=a,Format=format)
            attach.save()
            ls.Attachment.add(attach)
            ls.save()
        return redirect('pending-task')
    context = {
        'leads' : leads,
        'task' :task,
    }
    return render(request,'task-edit.html',context)

#################################################################################

@login_required
def view_pending_task(request,tid):
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    task = Task.objects.get(id=tid)
    replayes = Replays.objects.filter(Task=task)
    top = Replays.objects.filter(Task=task).first()

    if request.POST.get('date'):
        date = request.POST.get('date')
        description = request.POST.get('update-description')

        data = Replays(Date=d,AddedBy=user,Ip=ip,Task=task,Message=description,AddedDate=date)
        data.save()

        ld = Replays.objects.filter(Task=task).filter(AddedBy=user).last()
        attachment = request.FILES.getlist('attachment')
        for a in attachment:
            if str(a).endswith(('.png', '.jpg', '.jpeg')):
                format = 'image'
            else:
                format = 'file'
            attach = Attachments(Attachment=a,Name=a,Format=format)
            attach.save()
            ld.Attachments.add(attach)
            ld.save()
        return redirect('.')

    context = {
        'task' : task,
        'replayes' : replayes,
        'top' : top,
    }

    return render(request,'view-task-pending.html',context)

#################################################################################

@login_required
def view_completed_task(request,tid):
    task = Task.objects.get(id=tid)
    replayes = Replays.objects.filter(Task=task)
    top = Replays.objects.filter(Task=task).first()
    review = Review.objects.get(Task=task)
    context = {
        'task' : task,
        'replayes' : replayes,
        'review' : review,
        'top' : top,
    }
    return render(request,'view-task-completed.html',context)

#################################################################################

@login_required
def client_list(request):
    clients = Lead.objects.filter(Lead_Status=2).filter(Status=1)
    if request.method == 'POST':
        c = request.POST.get('c')
        lead= Lead.objects.get(id=c)
        lead.Status = 3
        lead.save()
        return redirect('clients')
    return render(request,'clients.html',{'clients':clients})

#################################################################################

@login_required
def client_view(request,cid):
    lead = Lead.objects.get(id=cid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    proposal = Proposal.objects.get(Lead=lead)
    # attachments = Attachments.objects.all()

    if request.method == 'POST':
        if request.POST.get('date'):
            date = request.POST.get('date')
            description = request.POST.get('update-description')

            data = Lead_Update(Date=d,AddedBy=user,Ip=ip,Lead=lead,Description=description,AddedDate=date)
            data.save()

            ld = Lead_Update.objects.filter(Lead=lead).filter(AddedBy=user).last()
            attachment = request.FILES.getlist('attachment')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                ld.Attachments.add(attach)
                ld.save()

        if request.POST.get('sdate'):
            sdate = request.POST.get('sdate')
            mode = request.POST.get('mode')
            ftime = request.POST.get('from')
            to = request.POST.get('to')
            sdescription = request.POST.get('sdescription')

            data = Lead_Schedule(Date=d,AddedBy=user,Ip=ip,Lead=lead,Mode=mode,From=ftime,To=to,Description=sdescription,AddedDate=sdate)
            data.save()

        if request.POST.get('udate'):
            udate = request.POST.get('udate')
            udescription = request.POST.get('u-description')
            participends = request.POST.get('participents')
            id = request.POST.get('id')
            meeting = Lead_Schedule.objects.get(id=id)
            meeting.Update_Description = udescription
            meeting.Update_Date = udate
            meeting.Members = participends
            meeting.save()

            attachment = request.FILES.getlist('attach')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                meeting.Attachment.add(attach)
                meeting.save()

        return redirect('/client-view/%s' %lead.id)

    schedules = Lead_Schedule.objects.filter(Lead=lead)

    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate >= dt.today() :
            upcoming.append(schedule)

    context = {
        'lead' : lead,
        'lead_update' : lead_update,
        # 'attachments' : attachments,
        'previous' : previous,
        'upcoming' : upcoming,
        'proposal' : proposal,
    }
    return render(request,'clients-view.html',context)

#################################################################################

@login_required
def accept(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Lead_Status = 3
    lead.To_Project = dt.today()
    lead.save()
    return redirect('projects')

#################################################################################

@login_required
def reject(request):
    pass

#################################################################################

@login_required
def projects(request):
    projects = Lead.objects.filter(Lead_Status=3).filter(Status=1)
    if request.method == 'POST':
        c = request.POST.get('c')
        lead= Lead.objects.get(id=c)
        lead.Status = 3
        lead.save()
        return redirect('projects')
    return render(request,'projects-list.html',{'projects':projects})

#################################################################################

@login_required
def view_project(request,pid):
    lead = Lead.objects.get(id=pid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    proposal = Proposal.objects.get(Lead=lead)
    # attachments = Attachments.objects.all()

    if request.method == 'POST':
        if request.POST.get('date'):
            date = request.POST.get('date')
            description = request.POST.get('update-description')

            data = Lead_Update(Date=d,AddedBy=user,Ip=ip,Lead=lead,Description=description,AddedDate=date)
            data.save()

            ld = Lead_Update.objects.filter(Lead=lead).filter(AddedBy=user).last()
            attachment = request.FILES.getlist('attachment')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                ld.Attachments.add(attach)
                ld.save()

        if request.POST.get('sdate'):
            sdate = request.POST.get('sdate')
            mode = request.POST.get('mode')
            ftime = request.POST.get('from')
            to = request.POST.get('to')
            sdescription = request.POST.get('sdescription')

            data = Lead_Schedule(Date=d,AddedBy=user,Ip=ip,Lead=lead,Mode=mode,From=ftime,To=to,Description=sdescription,AddedDate=sdate)
            data.save()

        if request.POST.get('udate'):
            udate = request.POST.get('udate')
            udescription = request.POST.get('u-description')
            participends = request.POST.get('participents')
            id = request.POST.get('id')
            meeting = Lead_Schedule.objects.get(id=id)
            meeting.Update_Description = udescription
            meeting.Update_Date = udate
            meeting.Members = participends
            meeting.save()

            attachment = request.FILES.getlist('attach')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                meeting.Attachment.add(attach)
                meeting.save()

        return redirect('/client-view/%s' %lead.id)

    schedules = Lead_Schedule.objects.filter(Lead=lead)

    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate >= dt.today() :
            upcoming.append(schedule)

    context = {
        'lead' : lead,
        'lead_update' : lead_update,
        # 'attachments' : attachments,
        'previous' : previous,
        'upcoming' : upcoming,
        'proposal' : proposal,
    }
    return render(request,'project-view.html',context)

#################################################################################

@login_required
def upcoming_meetings(request):
    schedules = Lead_Schedule.objects.filter(Status=1).order_by('AddedDate')
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    leads = Lead.objects.all()

    if request.method == 'POST':
        if request.POST.get('dste'):
            date = request.POST.get('date')
            mode = request.POST.get('mode')
            ftime = request.POST.get('from')
            to = request.POST.get('to')
            description = request.POST.get('description')
            l = request.POST.get('lead')
            lead = Lead.objects.get(id=l)

            data = Lead_Schedule(Date=d,AddedBy=user,Ip=ip,Lead=lead,Mode=mode,From=ftime,To=to,Description=description,AddedDate=date)
            data.save()
            return redirect('upcoming-meetings')

        if request.POST.get('id'):
            id = request.POST.get('id')
            meeting = Lead_Schedule.objects.get(id=id)
            meeting.Status = 0
            meeting.save()
            return redirect('upcoming-meetings')

    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate >= dt.today() :
            upcoming.append(schedule)
    return render(request,'meeting-upcoming.html',{'upcoming':upcoming,'leads':leads})

#################################################################################

@login_required
def previous_meetings(request):
    schedules = Lead_Schedule.objects.all().order_by('-AddedDate')
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    leads = Lead.objects.all()

    if request.method == 'POST':
        if request.POST.get('date'):
            date = request.POST.get('date')
            mode = request.POST.get('mode')
            ftime = request.POST.get('from')
            to = request.POST.get('to')
            description = request.POST.get('description')
            l = request.POST.get('lead')
            lead = Lead.objects.get(id=l)

            data = Lead_Schedule(Date=d,AddedBy=user,Ip=ip,Lead=lead,Mode=mode,From=ftime,To=to,Description=description,AddedDate=date)
            data.save()
            return redirect('.')
            
        if request.POST.get('udate'):
            udate = request.POST.get('udate')
            udescription = request.POST.get('udescription')
            participents = request.POST.get('participents')
            id = request.POST.get('id')
            meeting = Lead_Schedule.objects.get(id=id)
            meeting.Update_Description = udescription
            meeting.Update_Date = udate
            meeting.Members = participents
            meeting.save()

            attachment = request.FILES.getlist('attachment')
            for a in attachment:
                if str(a).endswith(('.png', '.jpg', '.jpeg')):
                    format = 'image'
                else:
                    format = 'file'
                attach = Attachments(Attachment=a,Name=a,Format=format)
                attach.save()
                meeting.Attachment.add(attach)
                meeting.save()

            return redirect('/previous-meeting-details/%s' %meeting.id)
        

    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate > dt.today() :
            upcoming.append(schedule)    
    return render(request,'meeting-previous.html',{'previous':previous,'leads':leads})

#################################################################################

@login_required
def meeting_staff_list(request):
    setreport()
    salesmans = User.objects.filter(is_salesman=True)
    reports = Salesman_Report.objects.filter(Status=1)
    return render(request,'meeting-staff.html',{'salesmans':salesmans,'reports':reports})

#################################################################################

@login_required
def meeting_staff_view(request,uid):
    salesman = User.objects.get(id=uid)
    schedules = Lead_Schedule.objects.filter(Lead__Salesman=salesman)
    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate >= dt.today() :
            upcoming.append(schedule)
    context = {
        'salesman':salesman,
        'previous' : previous,
        'upcoming' : upcoming,
    }
    return render(request,'meeting-staff-view.html',context)

#################################################################################


@login_required
def previous_meeting_details(request,mid):
    meeting = Lead_Schedule.objects.get(id=mid)
    return render(request,'meeting-previous-details.html',{'meeting':meeting})

#################################################################################

def task_staff(request):
    setreport()
    salesmans = User.objects.filter(is_salesman=True)
    reports = Salesman_Report.objects.filter(Status=1)
    return render(request,'task-staff.html',{'salesmans':salesmans,'reports':reports})

#################################################################################

def task_staff_view(request,uid):
    salesman = User.objects.get(id=uid)
    pending = Task.objects.filter(Lead__Salesman = salesman).filter(Task_Status=0)
    completed = Task.objects.filter(Lead__Salesman = salesman).filter(Task_Status=1)
    
    context = {
        'salesman' : salesman,
        'pending' : pending,
        'completed' : completed,
    }

    return render(request,'task-staff-view.html',context)

#################################################################################

@login_required
def salesman_report(request):
    reports = Salesman_Report.objects.filter(Status=1)
    return render(request,'salesman-report.html',{'reports':reports})

#################################################################################

@login_required
def salestarget(request):
    return render(request,'salestarget-report.html')

#################################################################################

@login_required
def target_report(request):
    return render(request,'target-report.html')

#################################################################################

@login_required
def top_customers(request):
    reports = Salesman_Report.objects.filter(Status=1)
    leads = Lead.objects.filter(Status=1).order_by('-ESValue')
    return render(request,'top-customers.html',{'reports':reports,'leads':leads})

#################################################################################

@login_required
def proposal_report(request):
    return render(request,'report-proposal.html')

#################################################################################

@login_required
def total_propose(request):
    reports = Lead.objects.filter(Status=1)
    return render(request,'report-proposal-total.html',{'reports':reports})

#################################################################################

@login_required
def remove_proposal_product(request,pid,id):
    product = Product.objects.get(id=id)
    proposal = Proposal.objects.get(id=pid)
    lid = proposal.Lead.id

    proposal.Products.remove(product)
    proposal.save()
    return redirect('/proposal/%s' %lid)

#################################################################################