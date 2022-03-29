from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout,handlers
from django.http import HttpResponseRedirect, JsonResponse

from Auth.froms.froms import userLogin,userRegister
from io import BytesIO
from utils.captcha import create_validate_code

def captcha(request):
    """
    获取验证码
    :param request:
    :return:
    """
    stream = BytesIO()
    # 生成图片 img、数字代码 code，保存在内存中，而不是 Django 项目中
    img, code = create_validate_code()
    img.save(stream, 'PNG')

    # 写入 session
    request.session['valid_code'] = code
    request.session.set_expiry(60) # session 的过期时间
    return HttpResponse(stream.getvalue())

def indexHome(request):
    executeInfo = {"status": "true", "msg": None}
    if request.method == "GET":
        userLoginInfo = userLogin()
        userRegisterInfo = userRegister()
        return render(request, "auth/auth.html", {"userLoginInfo": userLoginInfo, "userRegisterInfo":userRegisterInfo})
    elif request.method == "POST":
        if len(request.POST) > 3: # 注册
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
            code = request.POST["code"]
            if code.upper() == request.session.get('valid_code').upper():
                loginCheck = authenticate(username=username,password=password)
                if loginCheck is not None:
                    login(request, user=loginCheck)
                else:
                    executeInfo["status"] = "false"
                    executeInfo["msg"] = "用户密码有误，请重新输入！"
            else:
                executeInfo["status"] = "false"
                executeInfo["msg"] = "验证码输入错误，请重新输入！"
            return JsonResponse(executeInfo)

def toBase(request):
    if request.method == "GET":
        return render(request, "func_base.html", {"name": 1})