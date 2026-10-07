from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dbhubapp.models import *

import datetime

# Create your views here.

def digital_business_hub(request,id):
    if 'username' in request.session:
        username = request.session['username']
        print('username username',username)
        user_in_session = 1

        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
        context = {
        'dvh': dvh.objects.filter(id=id,flag=1),
        'datas': dvh.objects.filter(id=id,flag=1).first(),
        'user_in_session': user_in_session,
        }
        return render(request,'dphub/dphub_mgt/sample_page_dphub.html', context)
    else:
        username = request.session['username']
        print('username username', username)


        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id', user_id)
        context = {
            'dvh': dvh.objects.filter(id=id, flag=1),
            'datas': dvh.objects.filter(id=id, flag=1).first(),

        }
        return render(request, 'dphub/dbh_public_view/digital_business_hub.html', context)
