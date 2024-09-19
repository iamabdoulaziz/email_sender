from django.urls import path
from . import views

urlpatterns = [
    path('account', views.create_account, name='account'),
    path('login', views.login, name='login')
]
