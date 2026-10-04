from django.urls import path
from . import views
from . import enduser_login
from . import product_mgt
from . import dbhub_product_mgt

urlpatterns = [

    path('', views.index, name='index'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('login_request/', views.login_request, name='login_request'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('customer_login_request/', enduser_login.customer_login_request, name='customer_login_request'),
    path('customer_landing_page/', enduser_login.customer_landing_page, name='customer_landing_page'),

    # ****user start here *****
    path('view_all_users/', views.view_all_users, name='view_all_users'),
    path('create_user/', views.create_user, name='create_user'),
    path('user_regi/', views.user_regi, name='user_regi'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('user_update/<id>', views.user_update, name='user_update'),
    # ****user end here ******

    # ****end user start here *****
    path('view_all_endusers/', enduser_login.view_all_endusers, name='view_all_endusers'),
    path('create_enduser/', enduser_login.create_enduser, name='create_enduser'),
    path('enduser_regi/', enduser_login.enduser_regi, name='enduser_regi'),
    path('delete_enduser/<id>', enduser_login.delete_enduser, name='delete_enduser'),
    path('enduser_update/<id>', enduser_login.enduser_update, name='enduser_update'),
    # ****end user end here ******

    path('product_home_page/<id>', product_mgt.product_home_page, name='product_home_page'),

    path('view_all_dvc/<id>', product_mgt.view_all_dvc, name='view_all_dvc'),
    path('add_dvc/<id>', product_mgt.add_dvc, name='add_dvc'),
    path('dvc_regi/', product_mgt.dvc_regi, name='dvc_regi'),
    path('update_customer_dvc/<id>', product_mgt.update_customer_dvc, name='update_customer_dvc'),

    path('view_all_dvhub/<id>', dbhub_product_mgt.view_all_dvhub, name='view_all_dvhub'),
    path('add_dvhub/<id>', dbhub_product_mgt.add_dvhub, name='add_dvhub'),
    path('dbh_regi/', dbhub_product_mgt.dbh_regi, name='dbh_regi'),
    path('update_dphub/<id>', dbhub_product_mgt.update_dphub, name='update_dphub'),


    # logout
    path('logout/', views.logout, name='logout'),


]