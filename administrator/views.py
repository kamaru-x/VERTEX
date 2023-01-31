from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Category,Product,Lead,Lead_Update,Lead_Schedule,Attachments
from datetime import datetime,date
from datetime import date as dt
from django.contrib import messages
from u_auth.models import User

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
        count = Product.objects.filter(Category=category).count()
        category.Products = count
        category.save()

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
        date = datetime.date.today()
        user = request.user.id
        ip = setip(request)
        name = request.POST.get('name')

        value = Category(Date=date,AddedBy=user,Ip=ip,Name=name,Reference=refer)
        value.save()
        messages.success(request,'New category added successfully')
        return redirect('add-category')

    return render(request,'category-add.html',context)

#################################################################################

@login_required
def list_category(request):
    categories = Category.objects.filter(Status=1)
    context = {
        'categories' : categories
    }
    return render(request,'category-list.html',context)

#################################################################################

@login_required
def view_category(request,cid):
    category = Category.objects.get(id=cid)
    products = Product.objects.filter(Category=category).filter(Status=1)
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
        return redirect('.')
    context = {
        'category':category,
    }
    return render(request,'category-edit.html',context)

#################################################################################

@login_required
def delete_category(request,cid):
    category = Category.objects.get(id=cid)
    category.Status = 0
    category.save()
    return redirect('list-category')

#################################################################################

@login_required
def add_product(request):

    categories = Category.objects.all()
    r = Product.objects.last()
    date = datetime.date()
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

        c = Category.objects.get(id=category)

        value = Product(Date=date,AddedBy=user,Ip=ip,Category=c,Name=name,Price=price,Reference=refer)
        value.save()
        c.Products = c.Products+1
        c.save()

        messages.success(request,'new product added successfully')
        return redirect('add-product')
    
    context = {
        'refer':refer,
        'categories':categories,
    }

    return render(request,'product-add.html',context)

#################################################################################

@login_required
def list_products(request):
    products = Product.objects.filter(Status=1)
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
        product.Price = request.POST.get('price')
        product.save()
        setcount()

        messages.success(request,'product details edited successfully')
        return redirect('.')

    context = {
        'categories' : categories,
        'product' : product,
    }

    return render(request,'edit-product.html',context)

#################################################################################

@login_required
def delete_product(request,pid):
    product = Product.objects.get(id=pid)
    product.Status = 0
    product.save()
    return redirect('list-product')

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

        messages.success(request,'new supervisor created successfully')
        return redirect('add-salesman')

    return render(request,'salesman-add.html')

#################################################################################

@login_required
def list_salesman(request):
    salesmans = User.objects.exclude(is_superuser=True)
    context = {
        'salesmans':salesmans
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
        return redirect('.')

    context = {
        'salesman':salesman
    }
    return render(request,'edit-salesman.html',context)

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
        messages.success(request,'created new lead')
        return redirect('add-lead')

    context = {
        'refer':refer,
        'salesmans' : salesmans,
    }

    return render(request,'leads-add.html',context)

#################################################################################

@login_required
def list_leads(request):
    leads = Lead.objects.filter(Lead_Status=0)
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
                attach = Attachments(Attachment=a,Name='filename')
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
            participents = request.POST.get('participents')

            data = Lead_Schedule(Update_Date=udate,Update_Description=udescription,Members=participents)
            data.save()

            ls = Lead_Schedule.objects.filter(Lead=lead).filter(AddedBy=user).last()
            attachment = request.FILES.getlist('attach')
            for a in attachment:
                attach = Attachments(Attachment=a,Name='filename')
                attach.save()
                ls.Attachment.add(attach)
                ls.save()

        return redirect('/view-lead/%s' %lead.id)

    schedules = Lead_Schedule.objects.filter(Lead=lead)

    previous = []
    upcoming = []

    for schedule in schedules:
        if schedule.AddedDate < dt.today() :
            previous.append(schedule)
        elif schedule.AddedDate > dt.today() :
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
        return redirect('.')
    
    context = {
        'lead' : lead,
        'salesmans' : salesmans,
    }

    return render(request,'edit-lead.html',context)

#################################################################################

@login_required
def delete_lead(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Status = 0
    lead.save()
    return redirect('list-lead')

#################################################################################

@login_required
def opertunity_convertion(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Lead_Status = 1
    lead.To_Opertunity = date.today()
    lead.save()
    return redirect('list-lead')

#################################################################################

@login_required
def previous_meeting_details(request,mid):
    meeting = Lead_Schedule.objects.get(id=mid)
    return render(request,'meeting-previous-details.html',{'meeting':meeting})