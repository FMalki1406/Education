from django.shortcuts import reverse, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import User
# Create your views here.


@login_required
def home_view(request):
    if request.user.temp_pass:
        return HttpResponseRedirect(reverse('User:ChangePasswordPage'))
    else:
        if request.user.user_type in (1, 4):
            return HttpResponseRedirect(reverse('Staff:StaffHomePage'))
        # if request.user.user_type == 2:
        #     return HttpResponseRedirect(reverse('Instructor:StaffHomePage'))
        # if request.user.user_type == 3:
        #     return HttpResponseRedirect(reverse('Student:StudentHomePage'))


def login_view(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('User:HomePage'))
            else:
                messages.error(request, 'لم يتم تفعيل المستخدم')
        else:
            messages.error(request, 'اسم المتخدم أو كلمة المرور غير صحيحه')
    return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('User:LogInPage'))


def change_password_view(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 and password2 and password1 == password2:
            user = User.objects.get(username=request.user)
            user.set_password(password2)
            user.temp_pass = False
            user.save()
            return HttpResponseRedirect(reverse('User:HomePage'))
        else:
            messages.error(request, 'كلمة المرور غير متطابقه')
    return render(request, 'registration/change_password.html')

