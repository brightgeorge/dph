from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dbhubapp.models import *

import datetime

# Create your views here.

def view_all_upi_dbh(request,dbh_id):
    if 'username' in request.session:
        username = request.session['username']
        print('username username',username)
        user_in_session = 1
        print('user_in_session', user_in_session)

        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
        print('dbh_id dbh_id', dbh_id)
    else:
        user_in_session = 0
    context = {


    }
    return render(request,'dphub/upi/upi_mgt/view_all_upi_dbh.html', context)
