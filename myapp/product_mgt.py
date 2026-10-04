from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dvcapp.models import *
from dbhubapp.models import *


import datetime

# Create your views here.
def product_home_page(request,id):
    user = enduser_login.objects.get(id=id)
    user_id = user.id
    a = dvh.objects.filter(flag=1, user_id=user_id)
    b = dvc.objects.filter(flag=1, user_id=user_id)
    context = {
        'id': id,
        'a': len(a),
        'b': len(b),

    }
    return render(request,'product_mgt/product_home_page.html',context)

def view_all_dvc(request,id):
    user = enduser_login.objects.get(id=id)
    user_id = user.id
    print('user_id user_id', user_id)
    context = {
        #'dvcs': dvc.objects.filter(flag=1),
        'dvc': dvc.objects.filter(flag=1, user_id=user_id),
        'user_id': user_id,
        'sd': dvc.objects.get(flag=1, user_id=user_id),
    }
    return render(request,'product_mgt/digital_business_card/view_all_dvc.html', context)

def add_dvc(request, id):
    p = id
    print('iddd pp', p)
    #last = dvc.objects.order_by('-id').first()
    last = dvc.objects.filter(user_id=id)

    if last:
        #a = last.user_id
        #new_product_id = int(a) + 1
        new_product_id = len(last) + 1
    else:
        new_product_id = 1
    product_code = 'DVC'+str(id)+'/'+str(new_product_id)

    context = {
        'product_code': product_code,
        'id': id,
    }
    return render(request,'product_mgt/digital_business_card/add_dvc.html', context)


def dvc_regi(request):
    name = request.POST.get('name')
    chkitemname = dvc.objects.filter(name=name).exists()
    print('this is m y test uname',chkitemname)
    code= request.POST.get('code')
    chkemcod= dvc.objects.filter(code=code).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'Customer name and Plan Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Customer Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'Customer name already exists!. please try another one')
        return render(request, 'product_mgt/digital_business_card/view_all_dvc.html')
    else:
        if request.method == 'POST':
            id = request.POST.get('id')

            code = request.POST.get('code')
            user_id = request.POST.get('user_id')
            name = request.POST.get('name')
            mob = request.POST.get('mob')
            des = request.POST.get('description')

            uc = dvc()
            uc.code = code
            uc.user_id = user_id
            uc.name = name
            uc.mobile_number = mob
            uc.mobile_number_flag = 1
            uc.description = des
            uc.flag = 1
            uc.save()
            user = enduser_login.objects.get(id=id)
            user_id = user.id
            messages.info(request, 'Digital Business Card Plan  created sucessfully')
            context = {
                'dvc': dvc.objects.filter(flag=1, user_id=user_id),
                'id': id,
            }
            return render(request, 'product_mgt/digital_business_card/view_all_dvc.html', context)

    messages.info(request,'Digital Business Card Plan  created sucessfully')
    user = enduser_login.objects.get(id=id)
    user_id = user.id
    context = {
        'dvc': dvc.objects.filter(flag=1, user_id=user_id),
        'id': id,
    }
    return render(request,'product_mgt/digital_business_card/view_all_dvc.html', context)


def update_customer_dvc(request, id):
    name = request.POST.get('name')
    chkitemname = dvc.objects.filter(name=name).exists()
    print('this is m y test uname',chkitemname)
    code= request.POST.get('code')
    chkemcod= dvc.objects.filter(code=code).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'Customer name and Plan Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Customer Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'Customer name already exists!. please try another one')
        return render(request, 'product_mgt/digital_business_card/view_all_dvc.html')
    else:
        if request.method == 'POST':
            id = request.POST.get('id')

            code = request.POST.get('code')
            user_id = request.POST.get('user_id')
            name = request.POST.get('name')
            mob = request.POST.get('mob')
            des = request.POST.get('description')

            uc = dvc()
            uc.code = code
            uc.user_id = user_id
            uc.name = name
            uc.mobile_number = mob
            uc.mobile_number_flag = 1
            uc.description = des
            uc.flag = 1
            uc.save()
            user = enduser_login.objects.get(id=id)
            user_id = user.id
            messages.info(request, 'Digital Business Card Plan  created sucessfully')
            context = {
                'dvc': dvc.objects.filter(flag=1, user_id=user_id),
                'id': id,
            }
            return render(request, 'product_mgt/digital_business_card/view_all_dvc.html', context)

    messages.info(request,'Digital Business Card Plan  created sucessfully')
    user = enduser_login.objects.get(id=id)
    user_id = user.id
    context = {
        'dvc': dvc.objects.filter(flag=1, user_id=user_id),
        'id': id,
    }
    return render(request,'product_mgt/digital_business_card/update_customer_dvc.html', context)