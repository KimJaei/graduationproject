from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':   # POST 메소드의 요청이 들어오면
        if request.POST['password1'] == request.POST['password2']:   # password1과 password2의 POST 메소드로 요청된 값이 같다면
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('index')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        redirect('index')
    return render(request, 'index.html')