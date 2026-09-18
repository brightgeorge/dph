from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dvcapp.models import *


import datetime

# Create your views here.


def customer_login_request(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if enduser_login.objects.filter(username=username,password=password).exists():
            loginobj=enduser_login.objects.get(username=username,password=password)
            request.session['userid']=loginobj.id
            role=loginobj.role

            if role=='Customer':
                request.session['username'] = username
                us = request.session['username']
                import myapp
                #bgs = myapp.models.background_color.objects.all().filter(username=us)
                #bg = myapp.models.background_color.objects.all().filter(username=us).exists()
                #a = []
                #if bg == True:
                    #a.append(us)
                #else:
                    #a.append('f')

                context = {
                    #'bg': bgs,
                    #'us': us,
                    #'th_us': a[0],
                    'user': loginobj,
                    'name' : us
                }
                return render(request,'enduser_details/customer_landing_page.html', context)

            else:
                return render(request,'index.html',context={'user':loginobj})
        else:
            return render(request,'index.html',context={'msg':'User Name or Password Incorrect'})
    else:
        return render(request,'index.html')



def customer_landing_page(request):
    if 'username' in request.session:
        username = request.session['username']
        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
    context = {
        'dvc': dvc.objects.filter(flag=1, user_id=user_id)
    }
    return render(request,'enduser_details/customer_landing_page.html', context)





#************END USER SECTION STARTED HERE ***************

def view_all_endusers(request):
    if 'username' in request.session:
        context={
            'users': enduser_login.objects.filter(flag=1),
        }
        return render(request,'enduser_details/users/view_all_endusers.html',context)
    return render(request,'index.html')

def create_enduser(request):
    if 'username' in request.session:
        #last = customer_id.objects.order_by('-customer_id').first()
        last = enduser_login.objects.all()

        if last:
            #new_customer_id = last.customer_id + 1
            new_customer_id = len(last) + 1
        else:
            new_customer_id = 1

        #customer_id.objects.create(customer_id=new_customer_id)
        context = {
            'new_customer_id': new_customer_id,
        }
        return render(request,'enduser_details/users/enduser_creation.html',context)
    return render(request, 'index.html')

def enduser_regi(request):
    itname = request.POST.get('customer_name')
    chkitemname = enduser_login.objects.filter(username=itname).exists()
    print('this is m y test uname',chkitemname)
    empcod= request.POST.get('code')
    chkemcod= enduser_login.objects.filter(customer_id=empcod).exists()
    print('this is m y test user code', chkemcod)
    if chkitemname == True or chkemcod == True:
        if chkitemname == True and chkemcod == True:
            messages.info(request, 'User name and Employee Code both are already exists!. please try another one')
        if chkitemname == False and chkemcod == True:
            messages.info(request, 'Employee Code already exists!. please try another one')
        if chkitemname == True and chkemcod == False:
            messages.info(request, 'User name already exists!. please try another one')
        return render(request, 'enduser_details/users/enduser_creation.html', )
    else:
        if request.method == 'POST':
            code=request.POST.get('code')
            name = request.POST.get('name')
            uname = request.POST.get('username')
            upass = request.POST.get('password')
            description = request.POST.get('description')

            uc=enduser_login()
            uc.customer_id = code
            uc.customer_name = name
            uc.username = uname
            uc.password = upass
            uc.role = 'Customer'

            uc.customer_description=description
            uc.flag = 1
            uc.save()

    messages.info(request,'Customer created sucessfully')
    context = {
        'users': enduser_login.objects.filter(flag=1),
    }
    return render(request,'enduser_details/users/view_all_endusers.html',context)

def delete_enduser(request,id):
    if 'username' in request.session:
        de=enduser_login.objects.get(id=id)
        de.delete()
        messages.info(request, 'user deleted sucessfully')
        vu = enduser_login.objects.all()
        context = {
            'users': enduser_login.objects.filter(flag=1),
            'users': vu
        }
        return render(request, 'enduser_details/users/view_all_endusers.html', context)
    return render(request, 'index.html')

def enduser_update(request,id):
    if request.method == 'POST':
        ucode = request.POST.get('code')
        empname = request.POST.get('name')
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        urole = request.POST.get('role')

        udes = request.POST.get('description')
        fl = request.POST.get('eanable_disable')
        chk = 11
        if fl == None:
            chk = 0
        else:
            chk = 1
        uc = enduser_login.objects.get(id=id)
        uc.emp_id = ucode
        uc.emp_name = empname
        uc.username = uname
        uc.password = upass
        uc.role = urole

        uc.emp_description = udes
        uc.user_flage = chk
        uc.save()
        messages.info(request, 'user updated sucessfully')
        return view_all_endusers(request)

    context = {
        'users': enduser_login.objects.filter(flag=1),
        'sd': enduser_login.objects.get(id=id),
    }
    return render(request,'enduser_details/users/update_enduser.html',context)

#************END USER SECTION END HERE ***************

