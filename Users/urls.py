from django.urls import path
from . import views


app_name = 'User'

urlpatterns = [
    path('', views.home_view, name='HomePage'),
    path('login/', views.login_view, name='LogInPage'),
    path('logout/', views.logout_view, name='LogOutPage'),
    path('change_password/', views.change_password_view, name='ChangePasswordPage'),
]
