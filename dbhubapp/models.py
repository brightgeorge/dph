from django.db import models

# Create your models here.
class dvh(models.Model):
    code = models.CharField(max_length=250)
    user_id = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=250)

    digital_visiting_card = models.CharField(max_length=250)
    digital_visiting_card_flag = models.CharField(max_length=10)

    google_review = models.CharField(max_length=250)
    google_review_flag = models.CharField(max_length=10)
    instgram = models.CharField(max_length=250)
    instgram_flag = models.CharField(max_length=10)

    facebook = models.CharField(max_length=250)
    facebook_flag = models.CharField(max_length=10)
    whatsapp = models.CharField(max_length=250)
    whatsapp_flag = models.CharField(max_length=10)

    google_map = models.CharField(max_length=250)
    google_map_flag = models.CharField(max_length=10)
    website = models.CharField(max_length=250)
    website_flag = models.CharField(max_length=10)

    description = models.TextField()
    flag = models.IntegerField()
