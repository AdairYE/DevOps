from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,handlers
from django.http import HttpResponseRedirect, JsonResponse

from Auth.froms.froms import userLogin,userRegister


def indexHome(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        userLoginInfo = userLogin()
        userRegisterInfo = userRegister()
        return render(request, "auth/base.html", {"userLoginInfo": userLoginInfo,"userRegisterInfo":userRegisterInfo})
    elif request.method == "POST":
        if len(request.POST) > 2: # 注册
            userInfo = userRegister(request.POST)
            if userInfo.is_valid():
                userInfo.save()
            else:
                executeInfo["status"] = "false"
                executeInfo["msg"] = userInfo.errors
            return JsonResponse(executeInfo)
        else: # 登录
            username = request.POST["username"]
            password = request.POST["password"]
            loginCheck = authenticate(username=username,password=password)
            if loginCheck is not None:
                login(request, user=loginCheck)
            else:
                executeInfo["status"] = "false"
                executeInfo["msg"] = "用户密码有误，请重新输入！"
            return JsonResponse(executeInfo)

