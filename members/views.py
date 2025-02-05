from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, EditProfileForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.


def member_login(request):
    return render(request, 'members/login.html', {

    })


def member_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user_data = User.objects.filter(username=username)[0]
            print(username, password, email, user_data.id)

            # return HttpResponse(f'{user_data.username}, {user_data.email}')
            return redirect('members:profile', user_id=user_data.id)
    else:
        form = SignUpForm()
        print('Not working')

    return render(request, 'members/signup.html', {
        'form': form,
    })


def profile_page(request, user_id):
    print(user_id)
    current_user = User.objects.filter(id=user_id)[0]
    print(current_user.profile.first_name)
    return render(request, 'members/profile.html', {
        'data': current_user,
    })


def edit_profile(request, data_id):
    # print(data_id)
    data = Profile.objects.filter(user_id=data_id)[0]
    print(data.user_id)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            f_name = form.cleaned_data['first_name']
            print(f_name)
            return redirect('members:profile', user_id=data_id)

    else:
        form = EditProfileForm(instance=data)

    return render(request, 'members/editpro.html', {
        'form': form,
        'data': data
    })
