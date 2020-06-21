from django.urls import path

from .views import user_registration_send_email, create_user, login, change_password,check_if_user_exists

urlpatterns = [
    path('otp_register',user_registration_send_email),
    path('register', create_user),
    path('login', login),
    path('change_password',change_password),
    path('email/exists',check_if_user_exists)
]
