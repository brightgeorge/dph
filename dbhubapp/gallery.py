from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dbhubapp.models import *

import datetime

# Create your views here.
def dphub_gallery(request,id):
    if 'username' in request.session:
        username = request.session['username']
        print('username username',username)
        user_in_session = 1
        print('user_in_session', user_in_session)

        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
    else:
        user_in_session = 0
    context = {
        'dvh': dvh.objects.filter(id=id,flag=1),
        'datas': dvh.objects.filter(id=id,flag=1).first(),
        'user_in_session': user_in_session,
    }
    return render(request,'dphub/gallery/dphub_gallery.html', context)


def view_all_gallery_image_dbh(request,dbh_id):
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
        'dbh_id': dbh_id,
        'gallery_img': dbh_gallery.objects.filter(dbh_id=dbh_id,flag=1),

    }
    return render(request,'dphub/gallery/gallery_mgt/view_all_gallery_image_dbh.html', context)


def add_new_gallery_image_dbh(request,id):
    if 'username' in request.session:
        username = request.session['username']
        user = enduser_login.objects.get(username=username)
        user_id = user.id



    else:
        user_in_session = 0
    context = {
        'dbh_id': id,

    }
    return render(request,'dphub/gallery/gallery_mgt/add_new_gallery_image_dbh.html', context)

def add_new_gallery_image_dbh_regi(request):
    if 'username' in request.session:
        username = request.session['username']
        user = enduser_login.objects.get(username=username)
        user_id = user.id

        dbh_id = request.POST.get('dbh_code')
        google_drive_image_url = request.POST.get('google_drive_image_url')
        google_drive_image_heading = request.POST.get('google_drive_image_heading')
        google_drive_image_description = request.POST.get('google_drive_image_description')

        ic = dbh_gallery()
        ic.dbh_id = dbh_id
        ic.user_id =user_id
        ic.google_drive_image_url =google_drive_image_url
        ic.google_drive_image_heading = google_drive_image_heading
        ic.google_drive_image_description = google_drive_image_description
        ic.flag = 1
        ic.save()
        return view_all_gallery_image_dbh(request, dbh_id)

    else:
        user_in_session = 0
    context = {
        'dbh_id': id,

    }
    return render(request,'dphub/gallery/gallery_mgt/add_new_gallery_image_dbh.html', context)



def update_new_gallery_image_dbh(request,id,dbhid):
    if request.method == 'POST':
        username = request.session['username']
        user = enduser_login.objects.get(username=username)
        user_id = user.id

        dbh_id = request.POST.get('dbh_id')
        google_drive_image_url = request.POST.get('google_drive_image_url')
        google_drive_image_heading = request.POST.get('google_drive_image_heading')
        google_drive_image_description = request.POST.get('google_drive_image_description')

        ic = dbh_gallery.objects.get(id=id)
        #ic.dbh_id = dbh_id
        ic.user_id = user_id
        ic.google_drive_image_url = google_drive_image_url
        ic.google_drive_image_heading = google_drive_image_heading
        ic.google_drive_image_description = google_drive_image_description
        ic.flage = 1
        ic.save()
        return view_all_gallery_image_dbh(request, dbh_id)

    context = {
        'dbh_id': id,
        'sd': dbh_gallery.objects.get(id=id),
    }
    return render(request,'dphub/gallery/gallery_mgt/update_new_gallery_image_dbh.html',context)

def delete_new_gallery_image_dbh(request,id,dbhid):
    if 'username' in request.session:
        de=dbh_gallery.objects.get(id=id)
        de.delete()
        messages.info(request, 'user deleted sucessfully')
        context = {
            'dbh_id': dbhid,
            'gallery_img': dbh_gallery.objects.filter(dbh_id=dbhid, flag=1),

        }
        return render(request, 'dphub/gallery/gallery_mgt/view_all_gallery_image_dbh.html', context)


#************USER SECTION END HERE ***************

