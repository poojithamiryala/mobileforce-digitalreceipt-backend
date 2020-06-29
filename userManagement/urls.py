from django.urls import path

from .views import user_registration_send_email, create_user,logout, login, change_password,check_if_user_exists,create_notification,send_notification_now

urlpatterns = [
    path('otp_register',user_registration_send_email),
    path('register', create_user),
    path('login', login),
    path('change_password',change_password),
    path('logout', logout),
    path('email/exists',check_if_user_exists),
    path('notification/create',create_notification),
    path('notification/create/send/now', send_notification_now),

]
