from django.shortcuts import render
from django.contrib import messages

from myapp.models import *
from dvcapp.models import *

import datetime

# Create your views here.

def view_dvcards(request):
    username = request.session['username']
    user = enduser_login.objects.get(username=username)
    user_id = user.id
    context = {
        'dvc': dvc.objects.filter(flag=1, user_id=user_id)
    }
    return render(request,'dvcard/dvc_mgt/view_dvcards.html',context)

def view_dvcards_table(request):
    username = request.session['username']
    user = enduser_login.objects.get(username=username)
    user_id = user.id
    context = {
        'dvc': dvc.objects.filter(flag=1, user_id=user_id)
    }
    return render(request,'dvcard/dvc_mgt/view_dvcards_table.html',context)

def update_dvc_page(request,id):
    if 'username' in request.session:
        username = request.session['username']
        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
        if request.method == 'POST':
            username = request.session['username']
            user = enduser_login.objects.get(username=username)
            user_id = user.id

            name = request.POST.get('name')
            designation = request.POST.get('designation')
            designation_flag = request.POST.get('designation_flag')
            company_name = request.POST.get('company_name')
            company_name_flag = request.POST.get('company_name_flag')

            mobile_number = request.POST.get('mobile_number')
            mobile_number_flag = request.POST.get('mobile_number_flag')

            email_id = request.POST.get('email_id')
            email_id_flag = request.POST.get('email_id_flag')

            location_address = request.POST.get('location_address')
            location_address_flag = request.POST.get('location_address_flag')

            location_url = request.POST.get('location_url')
            location_url_flag = request.POST.get('location_url_flag')

            website_url = request.POST.get('website_url')
            website_url_flag = request.POST.get('website_url_flag')

            whatsapp = request.POST.get('whatsapp')
            whatsapp_flag = request.POST.get('whatsapp_flag')
            instagram = request.POST.get('instagram')
            instagram_flag = request.POST.get('instagram_flag')
            facebook = request.POST.get('facebook')
            facebook_flag = request.POST.get('facebook_flag')
            linkedin = request.POST.get('linkedin')
            linkedin_flag = request.POST.get('linkedin_flag')
            twitter = request.POST.get('twitter')
            twitter_flag = request.POST.get('twitter_flag')
            telegram = request.POST.get('telegram')
            telegram_flag = request.POST.get('telegram_flag')
            youtube = request.POST.get('youtube')
            youtube_flag = request.POST.get('youtube_flag')



            uc = dvc.objects.get(id=id)
            uc.user_id = user_id
            uc.name = name
            uc.name_flag = 1
            uc.designation = designation
            uc.designation_flag = designation_flag
            uc.company_name = company_name
            uc.company_name_flag = company_name_flag

            uc.mobile_number = mobile_number
            uc.mobile_number_flag = mobile_number_flag
            uc.email_id = email_id
            uc.email_id_flag = email_id_flag
            uc.location_address = location_address
            uc.location_address_flag = location_address_flag
            uc.location_url = location_url
            uc.location_url_flag = location_url_flag
            uc.website_url = website_url
            uc.website_url_flag = website_url_flag

            uc.whatsapp = whatsapp
            uc.whatsapp_flag = whatsapp_flag
            uc.instagram = instagram
            uc.instagram_flag = instagram_flag
            uc.facebook = facebook
            uc.facebook_flag = facebook_flag
            uc.linkedin = linkedin
            uc.linkedin_flag = linkedin_flag
            uc.twitter = twitter
            uc.twitter_flag = twitter_flag
            uc.telegram = telegram
            uc.telegram_flag = telegram_flag
            uc.youtube = youtube
            uc.youtube_flag = youtube_flag

            uc.flag = 1
            uc.save()
            messages.info(request, 'DVC updated sucessfully')
            return view_dvcards(request)

    context = {
        'dvc': dvc.objects.filter(id=id,flag=1, user_id=user_id),
        'sd': dvc.objects.get(id=id)
    }
    return render(request,'dvcard/dvc_mgt/update_dvc_page.html', context)

def update_dvc(request,id):
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

    messages.info(request, 'Digital Business Card Plan  created sucessfully')
    context = {
        'dvc': dvc.objects.filter(flag=1),
    }
    return render(request, 'plan_mgt/view_all_dvc_plan.html', context)



def sample_page_dvc(request,id):
    if 'username' in request.session:
        username = request.session['username']
        print('username username',username)


        user = enduser_login.objects.get(username=username)
        user_id = user.id
        print('user_id user_id',user_id)
    context = {
        'dvc': dvc.objects.filter(id=id,flag=1),
        'datas': dvc.objects.filter(id=id,flag=1).first(),
    }
    return render(request,'dvcard/dvc_mgt/sample_page_dvc.html', context)

#########################dvc_qr_generator start here###########

def dvc_qr_generator(request,id):
    context = {
        'datas': dvc.objects.filter(id=id, flag=1).first(),
    }

    return render(request,'dvcard/dvc_qr_mgt/dvc_qr_generator.html',context)




##########################dvc_qr_generator end here ###############