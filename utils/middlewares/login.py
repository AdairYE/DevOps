from django.utils.deprecation import MiddlewareMixin
from DevOps.settings import URL_WhiteList
from django.shortcuts import redirect

class LoginVerif(MiddlewareMixin):
    """
        登录校验
    """
    def process_request(self,request):

        if request.path not in URL_WhiteList:
            if not request.session.get("loginUser"):
                print("[ x ] 用户需要登录！")
                return redirect("/")
