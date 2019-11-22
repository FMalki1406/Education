from django.urls import path
from . import views

app_name = 'Staff'

urlpatterns = [
    path('', views.staff_home_view, name='StaffHomePage'),
    path('user/list/', views.user_list_view, name='ListUsersPage'),
    path('user/create/', views.user_create_view, name='UserCreatePage'),
    path('user/<int:pk>/delete', views.user_delete_view, name='UserDeletePage'),
    path('ministry/list/', views.ministry_list_view, name='MinistryListPage'),
    path('ministry/create/', views.ministry_create_view, name='MinistryCreatePage'),
    path('ministry/<int:pk>/update/', views.ministry_update_view, name='MinistryUpdatePage'),
]
