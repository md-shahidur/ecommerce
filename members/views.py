from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm
from django.contrib.auth.models import User

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

            print(username, password, email)
            return HttpResponse(f'{user_data.username}, {user_data.email}')
            # return redirect('front:home')
    else:
        form = SignUpForm()
        print('Not working')

    return render(request, 'members/signup.html', {
        'form': form,
    })
