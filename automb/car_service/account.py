from django.shortcuts import render

__author__ = 'Administrator'
from django.contrib.auth import authenticate, login

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        #test git
        if user.is_active:
            login(request, user)
            render(request,'car_service/')
        else:
            errmsg='该用户已被禁用,无法登录'

    else:
        errmsg='登录信息错误,请检查用户名和密码是否正确'

<<<<<<< HEAD

#modify
=======
>>>>>>> 5537a523b8dcb0236d2986e2e676f1d20ed87851
def logout(request):
    pass