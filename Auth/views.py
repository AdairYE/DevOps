from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect

# Create your views here.

def tologin(request):
    if request.method == "POST":
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        if username != None and password != None:
            loginCheck = authenticate(username=username,password=password)
            if loginCheck:
                login(request,user=loginCheck)
                return redirect('/admin/')
            else:
                errInfo = "登录失败，请重新登录!"
                return render(request, 'login/login.html',{"retcode":1,"err":errInfo})
    return render(request,'login/login.html')

def register(request):
    if request.method == "POST":
        reg_username = request.POST.get('reg_username',None)
        reg_password = request.POST.get('reg_password',None)
        reg_email = request.POST.get('reg_email',None)
        confirm_password = request.POST.get('confirm_password',None)
        user = User.objects.filter(username=reg_username).filter()
        if user:
            errInfo = "该用户已被注册！"
            return render(request, "login/register.html", {"retcode": 1, "err": errInfo})
        elif reg_username != None and reg_password != None:
            if reg_password == confirm_password:
                User.objects.create_user(
                    username=reg_username,
                    password=reg_password,
                    email=reg_email,
                )
                return HttpResponseRedirect("/login/",{"retcode":0,"info":"用户注册成功！"})
            else:
                errInfo = "两次密码不一致，请确认密码！"
                return render(request,"login/register.html",{"retcode":1,"err":errInfo})
        return render(request, "login/register.html", {"retcode": 0, "err": None})