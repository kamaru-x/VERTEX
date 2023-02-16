from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Category,Product,Lead,Lead_Update,Lead_Schedule,Attachments,Task,Salesman_Report,Review,Proposal,Sales_Target
from datetime import datetime,date
from datetime import date as dt
from django.contrib import messages
from u_auth.models import User
from datetime import timedelta

# Create your views here.

def setip(request):
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return(ip)

def setcount():
    categories = Category.objects.all()
    for category in categories:
        count = Product.objects.filter(Category=category).filter(Status=1).count()
        category.Products = count
        category.save()


# def setreport():
#     users = User.objects.filter(is_salesman=True)

#     ids = []

#     for u in users:
#         ids.append(u.id)
    
#     for i in ids:
#         user = User.objects.get(id=i)
#         report = Salesman_Report.objects.get(Salesman=user)

#         lead_total = Lead.objects.filter(Salesman=user).exclude(Status=0).count()
#         lead_failed = Lead.objects.filter(Salesman=user,Lead_Status=1,Status=3).count()
#         lead_success = lead_total - lead_failed

#         opportunity_total = lead_success
#         opportunity_failed = Lead.objects.filter(Salesman=user,Lead_Status=2,Status=3).count()
#         opportunity_success = opportunity_total - opportunity_failed

#         proposal_total = opportunity_success
#         proposal_failed = Lead.objects.filter(Salesman=user,Lead_Status=3,Status=3).count()
#         proposal_success = proposal_total - proposal_failed

#                             ##################################

#         report.Pending_Tasks = Task.objects.filter(Task_Status=0).filter(Lead__Salesman=user).count()
#         report.Completed_Tasks = Task.objects.filter(Task_Status=1).filter(Lead__Salesman=user).count()

#         report.Lead_Total = lead_total
#         report.Lead_Faild = lead_failed
#         report.Lead_Succes = lead_success

#         report.Opportunity_Total = opportunity_total
#         report.Opportunity_Success = opportunity_success
#         report.Opportunity_Faild = opportunity_failed

#         report.Proposal_Total = proposal_total
#         report.Proposal_Success = proposal_success
#         report.Proposal_Faild = proposal_failed

#         report.SV_Pending = 124651684 #Lead.objects.filter(Salesman=user).filter(Lead_Status=1).count()
#         report.SV_Success = 1398498498 #Lead.objects.filter(Salesman=user).filter(Lead_Status=2).count()
#         report.SV_Failed = 145168465 #Lead.objects.filter(Salesman=user).filter(Lead_Status=4).count()

#         schedules = Lead_Schedule.objects.filter(Lead__Salesman=user)
#         previous = []
#         upcoming = []

#         for schedule in schedules:
#             if schedule.AddedDate < dt.today() :
#                 previous.append(schedule)
#             elif schedule.AddedDate >= dt.today() :
#                 upcoming.append(schedule)

#         report.Upcoming_Meetings = len(upcoming)
#         report.Previous_Meetings = len(previous)

#         report.save()

def setmeeting():
    leads = Lead.objects.filter(Status=1)

    ids = []

    for l in leads:
        ids.append(l.id)
    
    for i in ids:
        lead = Lead.objects.get(id=i)
        schedules = Lead_Schedule.objects.filter(Lead=lead)
        previous = []
        upcoming = []

        for schedule in schedules:
            if schedule.AddedDate < dt.today() :
                previous.append(schedule)
            elif schedule.AddedDate >= dt.today() :
                upcoming.append(schedule)

        lead.Previous_Meetings = len(previous)
        lead.Upcoming_Meetings = len(upcoming)
        lead.save()


#################################################################################

@login_required
def add_category(request):

    r = Category.objects.last()

    if r:
        refer = f'REFERENCE-00{r.id+1}'
    else:
        refer = 'REFERENCE-001'
    
    context = {
        'refer':refer
    }

    if request.method == 'POST':
        date = dt.today()
        user = request.user.id
        ip = setip(request)
        name = request.POST.get('name')

        value = Category(Date=date,AddedBy=user,Ip=ip,Name=name,Reference=refer)
        value.save()
        messages.success(request,'New category added successfully')
        return redirect('list-category')

    return render(request,'category-add.html',context)

#################################################################################

@login_required
def list_category(request):
    categories = Category.objects.filter(Status=1).order_by('-id')

    if request.method == 'POST':
        id = request.POST.get('id')
        category = Category.objects.get(id=id)
        category.Status = 0
        category.save()
        return redirect('list-category')

    context = {
        'categories' : categories
    }
    return render(request,'category-list.html',context)

#################################################################################

@login_required
def view_category(request,cid):
    category = Category.objects.get(id=cid)
    products = Product.objects.filter(Category=category).filter(Status=1).order_by('-id')
    if request.method == 'POST':
        id = request.POST.get('id')
        product = Product.objects.get(id=id)
        product.Category = None
        product.save()
        setcount()
        return redirect('.')
    context = {
        'category' : category,
        'products' : products,
    }
    return render(request,'category-view.html',context)

#################################################################################

@login_required
def edit_category(request,cid):
    category = Category.objects.get(id=cid)
    if request.method == 'POST':
        category.Name = request.POST.get('name')
        category.save()
        return redirect('list-category')
    context = {
        'category':category,
    }
    return render(request,'category-edit.html',context)

#################################################################################

@login_required
def add_product(request):

    categories = Category.objects.filter(Status=1)
    r = Product.objects.last()
    date = dt.today()
    user = request.user.id
    ip = setip(request)

    if r:
        refer = f'PRODUCT-00{r.id+1}'
    else:
        refer = 'PRODUCT-001'

    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        price = request.POST.get('price')
        sprice = request.POST.get('sprice')
        description = request.POST.get('description')

        try:
            c = Category.objects.get(id=category)
        except:
            messages.error(request,'no category selected')
            return redirect('.')

        value = Product(Date=date,AddedBy=user,Ip=ip,Category=c,Name=name,Buying_Price=price,Selling_Price=sprice,Reference=refer,Description=description)
        value.save()
        c.Products = c.Products+1
        c.save()
        setcount()

        messages.success(request,'new product added successfully')
        return redirect('list-product')
    
    context = {
        'refer':refer,
        'categories':categories,
    }

    return render(request,'product-add.html',context)

#################################################################################

@login_required
def list_products(request):
    products = Product.objects.filter(Status=1).order_by('-id')
    if request.method == 'POST' :
        id = request.POST.get('id')
        product = Product.objects.get(id=id)
        product.Status = 0
        product.save()
        setcount()
        return redirect('list-product')
    context = {
        'products' : products
    }
    return render(request,'product-list.html',context)

#################################################################################

@login_required
def edit_product(request,pid):
    product = Product.objects.get(id=pid)
    user = request.user.id
    ip = setip(request)
    categories = Category.objects.filter(Status=1)

    if request.method == 'POST':
        product.EditedBy = user
        product.Edited_Date = date.today()
        product.EditedIp = ip
        category = request.POST.get('category')
        c = Category.objects.get(id=category)
        product.Category = c
        product.Name = request.POST.get('name')
        product.Buying_Price = request.POST.get('price')
        product.Selling_Price = request.POST.get('sprice')
        product.Description = request.POST.get('description')
        product.save()
        setcount()

        messages.success(request,'product details edited successfully')
        return redirect('list-product')

    context = {
        'categories' : categories,
        'product' : product,
    }

    return render(request,'edit-product.html',context)

#################################################################################

@login_required
def add_salesman(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        qid = request.POST.get('id-number')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        country = request.POST.get('country')

        password = '#password123'

        user = User.objects.create(first_name=name,Qatar_ID=qid,email=email,
        Mobile=mobile,Address=address,Country=country,is_salesman=True,username=email)
        user.save()
        user.set_password('#password123')
        user.save()

        salesman = User.objects.last()
        report = Salesman_Report(Salesman=salesman)
        report.save()

        messages.success(request,'new supervisor created successfully')
        return redirect('list-salesman')

    return render(request,'salesman-add.html')

#################################################################################

@login_required
def list_salesman(request):
    salesmans = User.objects.exclude(is_superuser=True).filter(is_active=True).order_by('-id')
    reports = Salesman_Report.objects.filter(Status=1)
    if request.method == 'POST' :
        id = request.POST.get('id')
        salesman = User.objects.get(id=id)
        salesman.is_active = False
        salesman.save()
        report = Salesman_Report.objects.get(Salesman=salesman)
        report.Status = 0
        report.save()
        return redirect('list-salesman')
    context = {
        'salesmans':salesmans,
        'reports' : reports,
    }
    return render(request,'salesman-list.html',context)

#################################################################################

@login_required
def edit_salesman(request,uid):
    salesman = User.objects.get(id=uid)
    if request.method == 'POST':
        salesman.first_name = request.POST.get('name')
        salesman.Qatar_ID = request.POST.get('id-number')
        salesman.email = request.POST.get('email')
        salesman.Mobile = request.POST.get('mobile')
        salesman.Address = request.POST.get('address')
        salesman.Country = request.POST.get('country')
        salesman.username = request.POST.get('email')
        salesman.save()
        messages.success(request,'salesman detail edited')
        return redirect('/salesman-view/%s' %salesman.id)

    context = {
        'salesman':salesman
    }
    return render(request,'edit-salesman.html',context)

#################################################################################

@login_required
def salesman_view(request,sid):
    setmeeting()
    salesman = User.objects.get(id=sid)
    schedules = Lead_Schedule.objects.filter(Lead__Salesman=salesman)
    leads = Lead.objects.filter(Salesman=salesman).filter(Lead_Status=0)
    opportunities = Lead.objects.filter(Salesman=salesman).filter(Lead_Status=1)
    clients = Lead.objects.filter(Salesman=salesman).filter(Lead_Status=2)
    projects = Lead.objects.filter(Salesman=salesman).filter(Lead_Status=3)
    p_task = Task.objects.filter(Lead__Salesman=salesman).filter(Task_Status=0).order_by('Due_Date')
    c_task = Task.objects.filter(Lead__Salesman=salesman).filter(Task_Status=1).order_by('-Completed_Date')

    t_count = len(p_task)

    if request.method == 'POST':

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

            return redirect('/salesman-view/%s/' %salesman.id)
    
        if request.POST.get('taskid'):
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
            return redirect('/salesman-view/%s/' %salesman.id)

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
        'leads' : leads,
        'opportunities' : opportunities,
        'clients' : clients,
        'projects' : projects,
        'ptasks' : p_task,
        'ctasks' : c_task,
        't_count' : t_count,
    }
    return render(request,'salesman-view.html',context)

#################################################################################

@login_required
def add_lead(request):
    user = request.user.id
    ip = setip(request)
    r = Lead.objects.last()
    salesmans = User.objects.filter(is_salesman=True)

    if r:
        refer = f'LEAD-00{r.id+1}'
    else:
        refer = 'LEAD-001'

    if request.method == 'POST':
        company = request.POST.get('company')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        ecdate = request.POST.get('date')
        esvalue = request.POST.get('value')
        state = request.POST.get('state')
        cname = request.POST.get('cname')
        cnumber = request.POST.get('cnumber')
        cmail = request.POST.get('cmail')
        salesman = request.POST.get('salesman')
        s = User.objects.get(id=salesman)


        data = Lead(Date=date.today(),AddedBy=user,Ip=ip,Reference=refer,Company=company,Address=address,
        Email=email,Phone=phone,ECDate=ecdate,ESValue=esvalue,State=state,CName=cname,CNumber=cnumber,
        CMail=cmail,Salesman=s)
        data.save()

        report = Salesman_Report.objects.get(Salesman=s)
        report.Lead_Total = report.Lead_Total+1
        report.save()

        messages.success(request,'created new lead')
        return redirect('list-lead')

    context = {
        'refer':refer,
        'salesmans' : salesmans,
    }

    return render(request,'leads-add.html',context)

#################################################################################

@login_required
def list_leads(request):
    setmeeting()
    leads = Lead.objects.filter(Lead_Status=0).filter(Status=1).order_by('-id')
    if request.method == 'POST' :
        if request.POST.get('id') :
            id = request.POST.get('id')
            lead = Lead.objects.get(id=id)
            lead.Status = 0
            lead.save()

            salesman = lead.Salesman
            report = Salesman_Report.objects.get(Salesman=salesman)
            report.Lead_Total = report.Lead_Total - 1
            report.save()
            return redirect('list-lead')
        
        if request.POST.get('c'):
            c = request.POST.get('c')
            lead= Lead.objects.get(id=c)
            lead.Status = 3
            lead.Cancel_Date = date.today()
            lead.Cancel_Reason = request.POST.get('reason')
            lead.save()

            salesman = lead.Salesman
            report = Salesman_Report.objects.get(Salesman=salesman)
            report.Lead_Faild = report.Lead_Faild + 1
            report.save()
            return redirect('list-lead')

    context = {
        'leads' : leads
    }
    return render(request,'leads-list.html',context)

#################################################################################

@login_required
def view_lead(request,lid):
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

        return redirect('/view-lead/%s' %lead.id)

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
    return render(request,'leads-view.html',context)

#################################################################################

@login_required
def edit_lead(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    ip = setip(request)
    salesmans = User.objects.filter(is_salesman=True)

    if request.method == 'POST':
        lead.EditedBy = user
        lead.EditedIp = ip
        lead.Company = request.POST.get('company')
        lead.Address = request.POST.get('address')
        lead.Email = request.POST.get('email')
        lead.Phone = request.POST.get('number')
        date = request.POST.get('date')
        temp = lead.Date
        if date:
            lead.ECDate = date
        else:
            lead.ECDate = temp
        # lead.ECDate = datetime.strptime(date, "%Y-%m-%d")
        lead.ESValue = request.POST.get('value')
        lead.State = request.POST.get('state')
        lead.CName = request.POST.get('cname')
        lead.CNumber = request.POST.get('cnumber')
        lead.CMail = request.POST.get('cmail')
        s = request.POST.get('salesman')
        salesman = User.objects.get(id=s)
        lead.Salesman = salesman
        lead.save()
        messages.success(request,'lead data edited successfull')
        return redirect('list-lead')
    
    context = {
        'lead' : lead,
        'salesmans' : salesmans,
    }

    return render(request,'edit-lead.html',context)

#################################################################################

@login_required
def opertunity_convertion(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Lead_Status = 1
    lead.To_Opertunity = date.today()
    lead.save()
    salesman = lead.Salesman
    report = Salesman_Report.objects.get(Salesman=salesman)
    report.Lead_Succes = report.Lead_Succes + 1
    report.Opportunity_Total = report.Opportunity_Total + 1
    report.save()
    return redirect('/opportunity-view/%s' %lead.id)

#################################################################################

def canceld_leads(request):
    leads = Lead.objects.filter(Lead_Status=0,Status=3)
    opportunities = Lead.objects.filter(Status=3,Lead_Status=1)
    clients = Lead.objects.filter(Status=3,Lead_Status=2)
    projects = Lead.objects.filter(Status=3,Lead_Status=3)

    context = {
        'leads':leads,
        'opportunities':opportunities,
        'clients':clients,
        'projects':projects,
    }

    return render(request,'canceld.html',context)

#################################################################################

@login_required
def view_canceled(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    # attachments = Attachments.objects.all()
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
    return render(request,'canceled_lead_view.html',context)

#################################################################################

@login_required
def canceled_opertunity_view(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    # attachments = Attachments.objects.all()
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
    return render(request,'canceled_opportunity_view.html',context)

#################################################################################

@login_required
def canceled_client_view(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    proposal = Proposal.objects.get(Lead=lead)
    # attachments = Attachments.objects.all()
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
    return render(request,'canceled_client_view.html',context)

#################################################################################

@login_required
def canceled_project_view(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    d = dt.today()
    ip = setip(request)
    lead_update = Lead_Update.objects.filter(Lead=lead)
    proposal = Proposal.objects.get(Lead=lead)
    # attachments = Attachments.objects.all()
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
    return render(request,'canceled_project_view.html',context)

#################################################################################

@login_required
def assign_target(request):
    targets = Sales_Target.objects.all()
    
    # total = []
    # archived = []
    # balance = []

    # data = []

    # for target in targets:
    #     years = []
    #     salesmans = []
    #     year = target.From.year
    #     years.append(year)
    #     yrs = [*set(years)]
    #     salesman = Sales_Target.objects.filter( From__year = year ).count()
    #     salesmans.append(salesman)
    # print(yrs)
    # print(salesmans)

    yrs = []

    for target in targets:
        yrs.append(target.From.year)
    years = [*set(yrs)]

    data = []

    for y in years :
        salesmans = Sales_Target.objects.filter(From__year = y).count()
        mans = Sales_Target.objects.filter(From__year = y )
        total = 0
        for man in mans:
            total = int(total + man.Targets)
        d = {'year':y,'salesmans':salesmans,'total':total}
        data.append(d)

    print(data)

    return render(request,'assign-target.html',{'data':data})

#################################################################################

@login_required
def target_setup(request):
    salesmans = User.objects.filter(is_salesman=True)

    if request.method == 'POST':
        salesman = request.POST.getlist('salesmans')
        targets = request.POST.getlist('targets')
        year = request.POST.get('year')

        Begindate = datetime.strptime(year, "%Y-%m-%d")
        Enddate = Begindate + timedelta(days=365)

        for (s , t) in zip(salesman,targets):
            man = User.objects.get(id=s)
            data = Sales_Target(Salesman=man,Targets=t,From=year,To=Enddate)
            data.save()
        return redirect('assign-target')

    context = {
        'salesmans' : salesmans,
    }

    return render(request,'target-setup.html',context)

#################################################################################

@login_required
def target_view(request,year):
    salesmans = Sales_Target.objects.filter(From__year = year)
    return render(request,'target-view.html',{'salesmans':salesmans,'year':year})

#################################################################################