from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.create_account, name='account'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('send_email/', views.send_email, name='send_email'),
    path("send_otp/", views.send_otp, name='send_otp'),
    path('verify_otp/', views.verify_otp, name='verify_otp')
]
