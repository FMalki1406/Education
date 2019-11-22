from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from Users.models import User, Ministry
from .forms import UserCreateForm, MinistryCreateForm
from django.contrib import messages

# Create your views here.


def staff_authenticated(user):
    if user:
        if user.is_anonymous:
            return False
        if user.user_type in (1, 4):
            return True
    return False


def staff_required(fn=None):
    decorator = user_passes_test(staff_authenticated)
    if fn:
        return decorator(fn)
    return decorator


@staff_required
def staff_home_view(request):
    return render(request, 'staff_base.html')


@staff_required
def user_list_view(request):
    context = {
        'users': User.objects.filter(is_active=True)
    }
    return render(request, 'users/users_list.html', context)


@staff_required
def user_create_view(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        user = User.objects.get(username=request.POST['username'])
        if not user:
            if form.is_valid():
                password = 123456
                User.objects.create_user(request.POST['username'], password=password)
                return HttpResponseRedirect(reverse('Staff:ListUsersPage'))
        else:
            messages.error(request, 'اسم المستخدم موجود مسبقا')

    form = UserCreateForm
    context = {
        'form': form
    }
    return render(request, 'users/user_create.html', context)


@staff_required
def user_delete_view(request, pk):
    user = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('Staff:ListUsersPage'))
    context = {
        'user_id': user.username
    }
    return render(request, 'users/user_delete.html', context)


@staff_required
def ministry_list_view(request):
    ministry = Ministry.objects.all()
    context = {
        'ministry': ministry
    }
    return render(request, 'ministry/ministry_list.html', context)


@staff_required
def ministry_create_view(request):
    if request.method == 'POST':
        form = MinistryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Staff:MinistryListPage'))
    context = {
        'form': MinistryCreateForm
    }
    return render(request, 'ministry/ministry_create.html', context)


@staff_required
def ministry_update_view(request, pk):
    ministry = get_object_or_404(Ministry, id=pk)
    print(ministry)
    form = MinistryCreateForm(request.POST or None, instance=ministry)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Staff:MinistryListPage'))
    context = {
        'form': form
    }
    return render(request, 'ministry/ministry_update.html', context)


