from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse

from Auth.froms.froms import userLogin


def indexHome(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        userLoginInfo = userLogin()
        return render(request, "auth/base.html", {"userLoginInfo": userLoginInfo})
    elif request.method == "POST":
        # 登录
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        loginCheck = authenticate(username=username, password=password)
        if loginCheck:
            login(request, user=loginCheck)
            return JsonResponse(executeInfo)
        else:
            executeInfo["status"] = "false"
            executeInfo["msg"] = "登录失败，请重新登录!"
            return JsonResponse(executeInfo)
