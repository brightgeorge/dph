from django.urls import path
from . import views
from . import enduser_login
from . import plan_mgt

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

    path('view_all_dvc_plan/', plan_mgt.view_all_dvc_plan, name='view_all_dvc_plan'),
    path('add_dvc_plan/<id>', plan_mgt.add_dvc_plan, name='add_dvc_plan'),
    path('dvc_plan_regi/', plan_mgt.dvc_plan_regi, name='dvc_plan_regi'),

    # logout
    path('logout/', views.logout, name='logout'),


]