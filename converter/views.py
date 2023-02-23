from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Lead,Lead_Schedule,Lead_Update,Attachments,Product,Task,Proposal,Replays,Salesman_Report,Review,Proposal_Items,Sales_Target
from u_auth.models import User
from datetime import date as dt
from administrator.views import setip
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from administrator.set_fun import setTarget
import math
from django.db.models import Sum

# Create your views here.

def set_proposals():
    leads = Lead.objects.filter(Status=1)
    for lead in leads:
        r_proposals = Proposal.objects.filter(Lead=lead).filter(Proposal_Status=0).count()
        a_proposals = Proposal.objects.filter(Lead=lead).filter(Proposal_Status=1).count()
        lead.Rejected_Proposals = r_proposals
        lead.Accepted_proposals = a_proposals
        lead.save()


@login_required
def list_opertunities(request):
    opertunities = Lead.objects.filter(Lead_Status=1).filter(Status=1).order_by('-id')
    if request.method == 'POST':
        c = request.POST.get('c')
        lead= Lead.objects.get(id=c)
        lead.Status = 3
        lead.Cancel_Date = dt.today()
        lead.Cancel_Reason = request.POST.get('reason')
        lead.save()

        # salesman = lead.Salesman
        # report = Salesman_Report.objects.get(Salesman=salesman)
        # report.Opportunity_Faild = report.Opportunity_Faild + 1
        # report.save()
        return redirect('list-opportunities')
    return render(request,'opportunity-list.html',{'opertunitunities':opertunities})

#################################################################################

@login_required
def view_opertunity(request,lid):
    set_proposals()
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
def proposal(request,lid):
    products = Product.objects.all()
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    r = Proposal.objects.last()

    if r:
        refer = f'PROPOSAL-00{r.id+1}'
    else:
        refer = 'PROPOSAL-001'

    proposal = Proposal(Date=d,AddedBy=user,Ip=ip,Lead=lead,Reference=refer)
    proposal.save()

    return redirect('/proposal/%s/' %proposal.id)

#################################################################################

@login_required
def create_proposal(request,lid):
    products = Product.objects.filter(Status=1)
    proposal = Proposal.objects.get(id=lid)
    lead = proposal.Lead
    pros = Proposal_Items.objects.filter(Proposal=proposal)
    
    if request.method == 'POST':
        if request.POST.get('product'):
            p = request.POST.get('product')
            pro = Product.objects.get(id=p)
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
            total = request.POST.get('total')
            # proposal.Grand_Total = request.POST.get('grand_total')
            # proposal.save()
            try:
                pr = Proposal_Items.objects.get(Proposal=proposal,Product=pro)
                if pr:
                    return redirect('/proposal/%s' %proposal.id)
            except:
                product = Proposal_Items(Proposal=proposal,Product=pro,Quantity=quantity,Sell_Price=price,Total=total)
                product.save()
                return redirect('/proposal/%s' %proposal.id)

        if request.POST.get('scope'):
            proposal.Scope = request.POST.get('scope')
            proposal.Payment = request.POST.get('payment')
            proposal.Exclusion = request.POST.get('exclusion')
            proposal.Terms_Condition = request.POST.get('terms')
            proposal.Grand_Total = request.POST.get('grand_total')
            proposal.save()
            return redirect('list-proposals')
        
        if request.POST.get('id'):
            id = request.POST.get('id')
            item = Proposal_Items.objects.get(id=id)
            item.delete()
            return redirect('/proposal/%s' %proposal.id)

    context = {
        'products' : products,
        'pros' : pros
    }
    return render(request,'proposal.html',context)

#################################################################################

@login_required
def list_proposals(request):
    set_proposals()
    proposals = Proposal.objects.filter(Status=1).order_by('-id')
    return render(request,'list_proposal.html',{'proposals':proposals})

#################################################################################

@login_required
def view_proposal(request,pid):
    proposal = Proposal.objects.get(id=pid)
    pros = Proposal_Items.objects.filter(Proposal=proposal)
    if request.method == 'POST':
        attachment = request.FILES.getlist('attachment')

        proposal.PO_Date = request.POST.get('today')
        proposal.PO_Number = request.POST.get('po-number')
        proposal.PO_Value = request.POST.get('po-value')
        proposal.Proposal_Status = 1
        proposal.save()

        lead = proposal.Lead
        lead.To_Client = dt.today()
        lead.Lead_Status = 2
        lead.save()

        for a in attachment:
            if str(a).endswith(('.png', '.jpg', '.jpeg')):
                format = 'image'
            else:
                format = 'file'
            attach = Attachments(Attachment=a,Name=a,Format=format)
            attach.save()
            proposal.Attachments.add(attach)
            proposal.save()
        
        # salesman = proposal.Lead.Salesman
        # report = Salesman_Report.objects.get(Salesman=salesman)
        # report.Proposal_Success = report.Proposal_Success + 1
        # report.save()

        return redirect('/view-proposal/%s/' %proposal.id)
    
    context = {
        'proposal' : proposal,
        'pros' : pros,
    }
    return render(request,'proposal_view.html',context)

#################################################################################

@login_required
def edit_proposal(request,pid):
    products = Product.objects.all()
    proposal = Proposal.objects.get(id=pid)
    lead = proposal.Lead
    pros = Proposal_Items.objects.filter(Proposal=proposal)
    
    if request.method == 'POST':
        if request.POST.get('product'):
            p = request.POST.get('product')
            pro = Product.objects.get(id=p)
            quantity = request.POST.get('quantity')
            price = request.POST.get('price')
            total = request.POST.get('total')
            try:
                pr = Proposal_Items.objects.get(Proposal=proposal,Product=pro)
                if pr:
                    return redirect('/proposal/%s' %proposal.id)
            except:
                product = Proposal_Items(Proposal=proposal,Product=pro,Quantity=quantity,Sell_Price=price,Total=total)
                product.save()
                return redirect('/proposal/%s' %proposal.id)
            
        if request.POST.get('id'):
            id = request.POST.get('id')
            item = Proposal_Items.objects.get(id=id)
            item.delete()
            return redirect('/proposal/%s' %proposal.id)

        proposal.Scope = request.POST.get('scope')
        proposal.Payment = request.POST.get('payment')
        proposal.Exclusion = request.POST.get('exclusion')
        proposal.Terms_Condition = request.POST.get('terms')
        proposal.Grand_Total = request.POST.get('grand_total')
        proposal.save()
        return redirect('list-proposals')

    context = {
        'products' : products,
        'pros' : pros,
        'proposal' : proposal,
    }

    return render(request,'proposal_edit.html',context)

#################################################################################

@login_required
def remove_proposal_product(request,pid,id):
    product = Product.objects.get(id=id)
    proposal = Proposal.objects.get(id=pid)
    lid = proposal.Lead.id
    return redirect('.')

#################################################################################

@login_required
def accept(request,pid):
    proposal = Proposal.objects.get(id=pid)
    proposal.Proposal_Status = 1
    proposal.save()
    lead = proposal.Lead
    lead.To_Client = dt.today()
    setTarget()

    # salesman = proposal.Lead.Salesman
    # report = Salesman_Report.objects.get(Salesman=salesman)
    # report.Proposal_Success = report.Proposal_Success + 1
    # report.save()
    return redirect('/client-view/%s' %lead.id)

#################################################################################

@login_required
def reject(request,pid):
    proposal = Proposal.objects.get(id=pid)
    proposal.Proposal_Status = 0
    proposal.save()

    setTarget()

    # salesman = proposal.Lead.Salesman
    # report = Salesman_Report.objects.get(Salesman=salesman)
    # report.Proposal_Faild = report.Proposal_Faild + 1
    # report.save()
    return redirect('/view-proposal/%s' %proposal.id)

#################################################################################

@login_required
def create_task(request):
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    leads = Lead.objects.filter(Status=1)
    salesmans = User.objects.filter(is_salesman=True)
    if request.method == 'POST':
        lead = request.POST.get('lead')
        salesman = request.POST.get('salesman')
        title = request.POST.get('title')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        description = request.POST.get('description')

        try:
            ld = Lead.objects.get(id=lead)
        except:
            return redirect('.')
        
        try:
            sm = User.objects.get(id=salesman)
        except:
            return redirect('.')

        data = Task(Date=d,AddedBy=user,Ip=ip,Lead=ld,Title=title,Priority=priority,Due_Date=date,Description=description,Salesman=sm)
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
        'leads' : leads,
        'salesmans' : salesmans,
    }
    return render(request,'create-task.html',context)

#################################################################################

@login_required
def pending_task(request):
    tasks = Task.objects.filter(Task_Status=0).filter(Status=1).order_by('Due_Date')
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
    tasks = Task.objects.filter(Task_Status=1).order_by('-Completed_Date')
    return render(request,'task-completed.html',{'tasks':tasks})

#################################################################################

@login_required
def edit_task(request,tid):
    task = Task.objects.get(id=tid)
    leads = Lead.objects.all()
    salesmans = User.objects.filter(is_salesman=True)
    user = request.user.id
    if request.method == 'POST':
        lead = request.POST.get('lead')
        salesman = request.POST.get('salesman')
        ld = Lead.objects.get(id=lead)
        sm = User.objects.get(id=salesman)

        task.Lead = ld
        task.Salesman = sm
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
        'task' : task,
        'salesmans' : salesmans,
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
    set_proposals()
    clients = Lead.objects.filter(Lead_Status=2).filter(Status=1).order_by('-id')
    if request.method == 'POST':
        c = request.POST.get('c')
        lead= Lead.objects.get(id=c)
        lead.Status = 3
        lead.Cancel_Date = dt.today()
        lead.Cancel_Reason = request.POST.get('reason')
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
    proposals = Proposal.objects.filter(Lead=lead)
    # attachments = Attachments.objects.all()
    count = Proposal.objects.filter(Lead=lead).count()

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
        'proposals' : proposals,
        'count' : count,
    }
    return render(request,'clients-view.html',context)

#################################################################################

@login_required
def projects(request):
    # projects = Lead.objects.filter(Lead_Status=3).filter(Status=1).order_by('-id')
    projects = Proposal.objects.filter(Proposal_Status=1).order_by('-id')
    # if request.method == 'POST':
    #     c = request.POST.get('c')
    #     lead= Lead.objects.get(id=c)
    #     lead.Status = 3
    #     lead.Cancel_Date = dt.today()
    #     lead.Cancel_Reason = request.POST.get('reason')
    #     lead.save()
    #     return redirect('projects')
    return render(request,'projects-list.html',{'projects':projects})

#################################################################################

@login_required
def view_project(request,pid):
    lead = Proposal.objects.filter(id=pid).last()
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead.Lead)
    proposal = Proposal.objects.get(id=pid)

    products = Proposal_Items.objects.filter(Proposal=proposal)
    catagories = []
    for product in products:
        catagories.append(product.Product.Category.Name)
        catagories = [*set(catagories)]

    context = {
        'lead' : lead,
        'lead_update' : lead_update,
        # 'attachments' : attachments,
        # 'previous' : previous,
        # 'upcoming' : upcoming,
        'proposal' : proposal,
        'catagories' : catagories,
        'products' : products,
    }
    return render(request,'project-view.html',context)

#################################################################################

@login_required
def upcoming_meetings(request):
    schedules = Lead_Schedule.objects.filter(Status=1).order_by('AddedDate')
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    leads = Lead.objects.filter(Status=1)

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

def edit_upcoming_meeting(request,id):
    meeting = Lead_Schedule.objects.get(id=id)
    leads = Lead.objects.filter(Status=1)

    if request.method == 'POST':
        meeting.AddedDate = request.POST.get('date')
        meeting.Mode = request.POST.get('mode')
        meeting.From = request.POST.get('from')
        meeting.To = request.POST.get('to')
        meeting.Description = request.POST.get('description')
        l = request.POST.get('lead')
        meeting.Lead = Lead.objects.get(id=l)
        meeting.save()
        return redirect('upcoming-meetings')

    context = {
        'meeting':meeting,
        'leads':leads,
    }
    return render(request,'meeting-upcoming-edit.html',context)

#################################################################################

@login_required
def previous_meetings(request):
    schedules = Lead_Schedule.objects.all().order_by('-AddedDate')
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    leads = Lead.objects.filter(Status=1)

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
    salesmans = User.objects.filter(is_salesman=True)
    reports = Salesman_Report.objects.filter(Status=1)
    return render(request,'task-staff.html',{'salesmans':salesmans,'reports':reports})

#################################################################################

def task_staff_view(request,uid):
    salesman = User.objects.get(id=uid)
    pending = Task.objects.filter(Salesman = salesman).filter(Task_Status=0)
    completed = Task.objects.filter(Salesman = salesman).filter(Task_Status=1)

    if request.method == "POST" :
        tid = request.POST.get('taskid')
        task = Task.objects.get(id=tid)
        date = request.POST.get('date')
        description = request.POST.get('update-description')
        task.Task_Status = 1
        task.Completed_Date = dt.today()
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
        return redirect('/task-staff/%s' %salesman.id)
    
    context = {
        'salesman' : salesman,
        'pending' : pending,
        'completed' : completed,
    }

    return render(request,'task-staff-view.html',context)

#################################################################################

@login_required
def salesman_report(request):
    reports = []
    salesmans = User.objects.filter(is_salesman=True)
    for salesman in salesmans:
        leads = Lead.objects.filter(Salesman=salesman).count()
        total_proposals = Proposal.objects.filter(Lead__Salesman=salesman)
        accepteted_proposals = Proposal.objects.filter(Lead__Salesman=salesman,Proposal_Status=1)
        rejected_proposals = Proposal.objects.filter(Lead__Salesman=salesman,Proposal_Status=0)

        sum_total_proposals = 0
        sum_accepteted_proposals = 0
        sum_rejected_proposals = 0

        for p in total_proposals:
            if p.Grand_Total:
                sum_total_proposals += p.Grand_Total

        for a in accepteted_proposals:
            if a.Grand_Total:
                sum_accepteted_proposals += a.Grand_Total
        
        for r in rejected_proposals:
            if r.Grand_Total:
                sum_rejected_proposals += r.Grand_Total

        report = {
            'salesman':salesman,
            'leads':leads,
            'total':total_proposals.count(),
            'accepteted_proposals':accepteted_proposals.count(),
            'rejected_proposals':rejected_proposals.count(),
            'sum_total_proposals':sum_total_proposals,
            'sum_accepteted_proposals':sum_accepteted_proposals,
            'sum_rejected_proposals':sum_rejected_proposals,
            }
        reports.append(report)
    return render(request,'salesman-report.html',{'reports':reports})

#################################################################################

@login_required
def salestarget(request):
    target = 0
    archived = 0
    balance = 0
    d = dt.today()
    year = d.year
    targets = Sales_Target.objects.filter(From__year=year)
    for t in targets:
        target += t.Targets
        archived += t.Archived
        balance = target - archived
    context = {
        'target' : target,
        'archived' : archived,
        'balance' : balance,
    }
    return render(request,'salestarget-report.html',context)

#################################################################################

@login_required
def target_report(request):
    salesmans = User.objects.filter(is_salesman = True)
    d = dt.today()
    y = d.year

    trgts = Sales_Target.objects.filter(From__year=y)
    targets = []
    setTarget()

    for t in trgts:

        if t.Targets and t.Archived != 0:
            p = (int(t.Targets) / int(t.Archived)) * 100
            percentage = math.trunc(p)
        else :
            percentage = 0

        target = {'Salesman':t.Salesman,'Targets':t.Targets,'Archived':t.Archived,'Pending':t.Balance,'Percentage':percentage}
        targets.append(target)

    context = {
        'targets' : targets
    }

    return render(request,'target-report.html',context)

#################################################################################

@login_required
def top_customers(request):
    lds = Lead.objects.filter(Status=1).order_by('-id')
    leads = []
    for lead in lds:
        volume = 0
        total_volume = 0
        proposals =  Proposal.objects.filter(Proposal_Status=1)
        a_proposals = Proposal.objects.filter(Lead=lead,Proposal_Status=1)

        for p in proposals:
            total_volume += p.Grand_Total

        for a in a_proposals:
            volume += a.Grand_Total

        if volume and total_volume != 0:
            p = volume / total_volume * 100
            percentage = math.trunc(p)
        else:
            percentage = 0

        company = {'Company':lead.Company,'Email':lead.Email,'Mobile':lead.Phone,'Reference':lead.Reference,'Salesman':lead.Salesman.first_name,'semail':lead.Salesman.email,'smobile':lead.Salesman.Mobile,'proposals':lead.Accepted_proposals+lead.Rejected_Proposals,'volume':volume,'Percentage':percentage}
        leads.append(company)
    return render(request,'top-customers.html',{'leads':leads})

#################################################################################

@login_required
def proposal_report(request):
    total = Proposal.objects.filter(Proposal_Status = 10).count()
    faild = Proposal.objects.filter(Proposal_Status = 0).count()
    success = Proposal.objects.filter(Proposal_Status = 1).count()

    proposals = Proposal.objects.all()

    total_value = 0
    failed_value = 0
    success_value = 0

    for proposal in proposals:
        if proposal.Proposal_Status == 10:
            if proposal.Grand_Total:
                total_value += proposal.Grand_Total

        if proposal.Proposal_Status == 1:
            if proposal.Grand_Total:
                success_value += proposal.Grand_Total

        if proposal.Proposal_Status == 0:
            if proposal.Grand_Total:
                failed_value += proposal.Grand_Total

    context = {
        'total' : total,
        'faild' : faild,
        'success' : success,
        'total_value' : total_value,
        'failed_value' : failed_value,
        'success_value' : success_value,
    }

    return render(request,'report-proposal.html',context)

#################################################################################

@login_required
def total_propose(request):
    proposals = Proposal.objects.filter(Status=1)
    return render(request,'report-proposal-total.html',{'proposals':proposals})

#################################################################################

@csrf_exempt
def get_product_data(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        pro = Product.objects.get(id=id)

        product = {'id':pro.id,'price':pro.Buying_Price,'sprice':pro.Selling_Price}
        return JsonResponse(product)

#################################################################################