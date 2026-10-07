from django.urls import path
from . import views
from . import dbh
from . import dbh_public_view

urlpatterns = [
    path('view_dphub/', dbh.view_dphub, name='view_dphub'),


    path('sample_page_dphub/<id>', dbh.sample_page_dphub, name='sample_page_dphub'),
    path('customer_update_dph_page/<id>', dbh.customer_update_dph_page, name='customer_update_dph_page'),

    path('dbh_qr_generator/<id>', dbh.dbh_qr_generator, name='dbh_qr_generator'),


    path('digital_business_hub/<id>', dbh_public_view.digital_business_hub, name='digital_business_hub'),


    ]