from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import widgets as wid
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from DevOps.forms import baseFroms




class userLogin(baseFroms, forms.ModelForm):
    code = forms.CharField(
        label="验证码"
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=32,
        error_messages={
            "min_length": "密码长度不能小于8个字符",
            "max_length": "密码长度不能大于32个字符"
        }
    )

    class Meta:
        model = User
        fields = ["username", "password", "code"]


class userRegister(baseFroms, forms.ModelForm):
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=32,
        error_messages={
            "min_length": "密码长度不能小于8个字符",
            "max_length": "密码长度不能大于32个字符"
        }
    )
    againPassword = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=32,
        error_messages={
            "min_length": "密码长度不能小于8个字符",
            "max_length": "密码长度不能大于32个字符"
        }
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "againPassword"]

    def clean_againPassword(self):
        password = self.cleaned_data["password"]
        againPassword = self.cleaned_data["againPassword"]

        # check_password 方法可以校验明文密码是否与密文密码一致；第一个是明文，第二个是密文
        if not check_password(againPassword, password):
            raise ValidationError("两次密码输入不一致，请重新输入！")

        return againPassword

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not password:
            raise ValidationError("密码不能为空！")

        # make_password 可对明文密码进行加密，同一密码加密结果不一致
        password = make_password(password)

        return password
