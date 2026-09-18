from django.db import models

# Create your models here.


class dvc(models.Model):
    code = models.CharField(max_length=250)
    user_id = models.CharField(max_length=250)

    name = models.CharField(max_length=250)
    name_flag = models.CharField(max_length=10)
    designation = models.CharField(max_length=250)
    designation_flag = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    company_name_flag = models.CharField(max_length=250)

    mobile_number = models.CharField(max_length=250)
    mobile_number_flag = models.CharField(max_length=250)
    email_id = models.CharField(max_length=250)
    email_id_flag = models.CharField(max_length=250)
    location_address = models.CharField(max_length=250)
    location_address_flag = models.CharField(max_length=250)
    location_url = models.CharField(max_length=250)
    location_url_flag = models.CharField(max_length=250)
    website_url = models.CharField(max_length=250)
    website_url_flag = models.CharField(max_length=250)


    whatsapp = models.CharField(max_length=250)
    whatsapp_flag = models.CharField(max_length=250)
    instagram = models.CharField(max_length=250)
    instagram_flag = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    facebook_flag = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    linkedin_flag = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    twitter_flag = models.CharField(max_length=250)
    telegram = models.CharField(max_length=250)
    telegram_flag = models.CharField(max_length=250)
    youtube = models.CharField(max_length=250)
    youtube_flag = models.CharField(max_length=250)

    description = models.TextField()
    flag = models.IntegerField()

