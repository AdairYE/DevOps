from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse

from Auth.froms.froms import userLogin,userRegister


def indexHome(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        userLoginInfo = userLogin()
        userRegisterInfo = userRegister()
        return render(request, "auth/base.html", {"userLoginInfo": userLoginInfo,"userRegisterInfo":userRegisterInfo})
    elif request.method == "POST":
        if len(request.POST) > 2:
            userInfo = userRegister(request.POST)
            if userInfo.is_valid():
                userInfo.save()
            else:
                executeInfo["status"] = "false"
                executeInfo["msg"] = userInfo.errors
            return JsonResponse(executeInfo)
        else:
            userInfo = userLogin(request.POST)
            if userInfo.is_valid():
                validInfo = userInfo.cleaned_data
                username = validInfo["username"]
                password =validInfo["password"]
                loginCheck = authenticate(username=username, password=password)
                if loginCheck:
                    login(request, user=loginCheck)
                else:
                    executeInfo["status"] = "false"
                    executeInfo["msg"] = "登录失败，请重新登录!"
            return JsonResponse(executeInfo)

        # # 登录
        # username = request.POST.get("username", None)
        # password = request.POST.get("password", None)
        # loginCheck = authenticate(username=username, password=password)
        # if loginCheck:
        #     login(request, user=loginCheck)
        #     return JsonResponse(executeInfo)
        # else:
        #     executeInfo["status"] = "false"
        #     executeInfo["msg"] = "登录失败，请重新登录!"
        #     return JsonResponse(executeInfo)
