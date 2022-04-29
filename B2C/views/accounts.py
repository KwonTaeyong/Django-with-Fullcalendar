from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def account(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(
                id=request.POST['id'],
                password=request.POST['password'],
                name=request.POST['name'],
            )
            auth.login(request,user)
            return redirect('/')
        return render(request, 'common/accounts.html')
    return render(request, 'common/accounts.html')