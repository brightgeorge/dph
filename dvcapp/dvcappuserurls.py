#dvcappuserurls
from django.urls import path
from . import dvc

urlpatterns = [

    path('view_dvcards/', dvc.view_dvcards, name='view_dvcards'),
    path('view_dvcards_table/', dvc.view_dvcards_table, name='view_dvcards_table'),

    path('update_dvc_page/<id>', dvc.update_dvc_page, name='update_dvc_page'),
    path('update_dvc/<id>', dvc.update_dvc, name='update_dvc'),
    path('sample_page_dvc/<id>', dvc.sample_page_dvc, name='sample_page_dvc'),


    path('dvc_qr_generator/<id>', dvc.dvc_qr_generator, name='dvc_qr_generator'),



    ]