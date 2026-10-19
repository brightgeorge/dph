from django.urls import path
from . import views
from . import dbh
from . import dbh_public_view
from . import gallery
from . import upi

urlpatterns = [
    path('view_dphub/', dbh.view_dphub, name='view_dphub'),


    path('sample_page_dphub/<id>', dbh.sample_page_dphub, name='sample_page_dphub'),
    path('customer_update_dph_page/<id>', dbh.customer_update_dph_page, name='customer_update_dph_page'),

    path('dbh_qr_generator/<id>', dbh.dbh_qr_generator, name='dbh_qr_generator'),


    path('digital_business_hub/<id>', dbh_public_view.digital_business_hub, name='digital_business_hub'),

    path('dphub_gallery/<id>', gallery.dphub_gallery, name='dphub_gallery'),
    path('view_all_gallery_image_dbh/<dbh_id>', gallery.view_all_gallery_image_dbh, name='view_all_gallery_image_dbh'),
    path('add_new_gallery_image_dbh/<id>', gallery.add_new_gallery_image_dbh, name='add_new_gallery_image_dbh'),
    path('add_new_gallery_image_dbh_regi/', gallery.add_new_gallery_image_dbh_regi, name='add_new_gallery_image_dbh_regi'),

    path('update_new_gallery_image_dbh/<id>/<dbhid>', gallery.update_new_gallery_image_dbh, name='update_new_gallery_image_dbh'),
    path('delete_new_gallery_image_dbh/<id>/<dbhid>', gallery.delete_new_gallery_image_dbh, name='delete_new_gallery_image_dbh'),
    path('view_all_upi_dbh/<dbh_id>', upi.view_all_upi_dbh, name='view_all_upi_dbh'),

    ]