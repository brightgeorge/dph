from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dbhubapp.models import *

import datetime

# Create your views here.

def view_dphub(request):
    username = request.session['username']
    user = enduser_login.objects.get(username=username)
    user_id = user.id
    context = {
        'dvc': dvh.objects.filter(flag=1, user_id=user_id)
    }
    return render(request,'dphub/dphub_mgt/view_dphub.html',context)

def sample_page_dphub(request,id):
    if 'username' in request.session:
        username = request.session['username']
        print('username username',username)

        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
    context = {
        'dvh': dvh.objects.filter(id=id,flag=1),
        'datas': dvh.objects.filter(id=id,flag=1).first(),
    }
    return render(request,'dphub/dphub_mgt/sample_page_dphub.html', context)


def customer_update_dph_page(request,id):
    if 'username' in request.session:
        username = request.session['username']
        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
        if request.method == 'POST':
            username = request.session['username']
            user = enduser_login.objects.get(username=username)
            user_id = user.id

            company_name = request.POST.get('company_name')

            digital_visiting_card = request.POST.get('digital_visiting_card')
            digital_visiting_card_flag = request.POST.get('digital_visiting_card_flag')

            google_review = request.POST.get('google_review')
            google_review_flag = request.POST.get('google_review_flag')
            instgram = request.POST.get('instgram')
            instgram_flag = request.POST.get('instgram_flag')

            facebook = request.POST.get('facebook')
            facebook_flag = request.POST.get('facebook_flag')
            print('facebook facebook', facebook)
            whatsapp = request.POST.get('whatsapp')
            whatsapp_flag = request.POST.get('whatsapp_flag')


            google_map = request.POST.get('google_map')
            google_map_flag = request.POST.get('google_map_flag')
            website = request.POST.get('website')
            website_flag = request.POST.get('website_flag')


            #website_url = request.POST.get('website_url')
            #website_url_flag = request.POST.get('website_url_flag')





            uc = dvh.objects.get(id=id)
            uc.user_id = user_id

            uc.company_name = company_name
            uc.digital_visiting_card = digital_visiting_card
            uc.digital_visiting_card_flag = digital_visiting_card_flag

            uc.google_review = google_review
            uc.google_review_flag = google_review_flag
            uc.instgram = instgram
            uc.instgram_flag = instgram_flag

            uc.facebook = facebook
            uc.facebook_flag = facebook_flag
            uc.whatsapp = whatsapp
            uc.whatsapp_flag = whatsapp_flag


            uc.google_map = google_map
            uc.google_map_flag = google_map_flag
            uc.website = website
            uc.website_flag = website_flag

            #uc.website_url = website_url
            #uc.website_url_flag = website_url_flag



            uc.flag = 1
            uc.save()
            messages.info(request, 'DPAHub updated sucessfully')
            return view_dphub(request)

    context = {
        'dvh': dvh.objects.filter(id=id,flag=1, user_id=user_id),
        'sd': dvh.objects.get(id=id)
    }
    return render(request,'dphub/dphub_mgt/customer_update_dph_page.html', context)

#########################dvc_qr_generator start here###########

def dbh_qr_generator(request,id):
    context = {
        'datas': dvh.objects.filter(id=id, flag=1).first(),
    }

    return render(request,'dphub/dbh_qr_mgt/dbh_qr_generator.html',context)




##########################dvc_qr_generator end here ###############
