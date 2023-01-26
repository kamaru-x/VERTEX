from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Category,Product,Lead
import datetime
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
    date = datetime.date.today()
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
    date = datetime.date.today()
    categories = Category.objects.filter(Status=1)

    if request.method == 'POST':
        product.EditedBy = user
        product.Edited_Date = date
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
        Mobile=mobile,Address=address,Country=country,is_staff=True,username=email)
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
    date = datetime.date.today()
    r = Lead.objects.last()

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

        data = Lead(Date=date,AddedBy=user,Ip=ip,Reference=refer,Company=company,Address=address,
        Email=email,Phone=phone,ECDate=date,ESValue=esvalue,State=state)
        data.save()
        messages.success(request,'created new lead')
        return redirect('add-lead')

    context = {
        'refer':refer
    }

    return render(request,'leads-add.html',context)

#################################################################################

@login_required
def list_leads(request):
    leads = Lead.objects.all()
    context = {
        'leads' : leads
    }
    return render(request,'leads-list.html',context)

#################################################################################

@login_required
def edit_lead(request,lid):
    lead = Lead.objects.get(id=lid)
    user = request.user.id
    ip = setip(request)
    date = datetime.date.today()

    if request.method == 'POST':
        lead.EditedBy = user
        lead.EditedIp = ip
        lead.Company = request.POST.get('company')
        lead.Address = request.POST.get('address')
        lead.Email = request.POST.get('email')
        lead.Phone = request.POST.get('number')
        lead.ECDate = date
        lead.ESValue = request.POST.get('value')
        lead.State = request.POST.get('state')
        lead.save()
        messages.success(request,'lead data edited successfull')
        return redirect('.')
    
    context = {
        'lead' : lead
    }

    return render(request,'edit-lead.html',context)

#################################################################################

@login_required
def delete_lead(request,lid):
    lead = Lead.objects.get(id=lid)
    lead.Status = 0
    lead.save()
    return redirect('list-lead')