from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dvcapp.models import *


import datetime

# Create your views here.

def view_all_dvc_plan(request):
    return render(request,'plan_mgt/view_all_dvc_plan.html')

def add_dvc_plan(request, id):
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
    return render(request,'plan_mgt/add_dvc_plan.html', context)


def dvc_plan_regi(request):
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
        return render(request, 'plan_mgt/view_all_dvc_plan.html')
    else:
        if request.method == 'POST':
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

    messages.info(request,'Digital Business Card Plan  created sucessfully')
    context = {
        'dvc': dvc.objects.filter(flag=1),
    }
    return render(request,'plan_mgt/view_all_dvc_plan.html', context)


