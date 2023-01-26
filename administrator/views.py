from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from administrator.models import Category,Product
import datetime
from django.contrib import messages

# Create your views here.

def setip(request):
    x_forw_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forw_for is not None:
        ip = x_forw_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return(ip)

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