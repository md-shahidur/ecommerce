from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def member_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # return redirect('members:profile', user_id=user.id)
            return redirect('front:home')
    return render(request, 'members/login.html', {

    })


@login_required
def member_logout(request):
    logout(request)
    return redirect('front:home')


def member_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # email = form.cleaned_data['email']
            user = authenticate(request, username=username, password=password)
            # user.profile.email = email
            if user is not None:
                login(request, user)
                print(user.id)
                return redirect('members:edit_profile', data_id=user.id)

            # user_data = User.objects.filter(username=username)[0]
            # print(username, password, email, user_data.id)

            # return HttpResponse(f'{user_data.username}, {user_data.email}')
            # return redirect('members:profile', user_id=user_data.id)
    else:
        form = SignUpForm()
        print('Not working')

    return render(request, 'members/signup.html', {
        'form': form,
    })


@login_required
def profile_page(request, user_id):
    print(user_id)
    current_user = User.objects.filter(id=user_id)[0]
    print(current_user.profile.gender)
    return render(request, 'members/profile.html', {
        'data': current_user,
    })


@login_required
def edit_profile(request, data_id):
    print(data_id)
    data = Profile.objects.filter(user_id=data_id)[0]
    print(data.user_id)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data['first_name']
            gen = form.cleaned_data['gender']
            print(f_name, gen)
            print(type(gen))
            return redirect('members:profile', user_id=data_id)

    else:
        form = EditProfileForm(instance=data)

    return render(request, 'members/editpro.html', {
        'form': form,
        'data': data
    })
