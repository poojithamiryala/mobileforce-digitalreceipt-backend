from django.urls import path

from .views import user_registration_send_email, create_user

urlpatterns = [
    path('otp_register',user_registration_send_email),
    path('register', create_user)
]
