from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .  import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('singin',views.singin,name='singin'),
    path('send_parcel',views.send_parcel,name='send_parcel'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('admin',views.admin,name='admin'),
    path('logoutUser',views.logoutUser,name='logoutUser'),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('admin/new_order_admin',views.new_order_admin,name='new_order_admin'),

    path('admin/deliver',views.deliver,name='deliver'),
    path('admin/hold',views.hold,name='hold'),
    path('admin/in_transit',views.in_transit,name='in_transit'),
    path('admin/active_user',views.active_user, name='active_user'),
    path('admin/payments/<str:pk>/',views.payments, name='payments'),
    path('admin/make_payment/<str:pk>/',views.make_payment, name='make_payment'),



# user dashboard
    path('new_order',views.new_order, name='new_order'),
    path('all_order_user',views.all_order_user, name='all_order_user'),
    path('delete_order/<str:pk>/',views.delete_order, name='delete_order'),
    path('Update_order_user/<str:pk>/',views.Update_order_user, name='Update_order_user'),




    path('profile/',views.profile,name='profile'),



    

    path('admin/make_order',views.make_order, name='make_order'),

# password  reset
    path('reset_password/',auth_views.PasswordResetView.as_view( template_name='forgot_password.html' ) , name="reset_password"),

    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view( template_name='password_reset_sent.html' ) , name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view( template_name='password_reset_form.html' ) , name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view( template_name='password_reset_done.html') , name="password_reset_complete"),




    path('track',views.track,name='track'),


    







    path('order_confirm',views.order_confirm,name='order_confirm'),
    path('test',views.test,name='test'),


]
