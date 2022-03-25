from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import widgets as wid
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout


class userLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": wid.TextInput(attrs={'class': 'form-control'}),
            "password": wid.PasswordInput(attrs={'class': 'form-control'}),
        }

class userRegister(forms.ModelForm):
    againPassword = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(),
        min_length=8,
        max_length=32,
        error_messages={
            "min_length":"密码长度不能小于8个字符",
            "max_length":"密码长度不能大于32个字符"
        }
    )

    class Meta:
        model = User
        fields = ["username","email","password","againPassword"]
        widgets = {
            "password": wid.PasswordInput(attrs={'class': 'form-control'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "请输入{}".format(field.label)

    def clean_againPassword(self):
        againPassword = self.cleaned_data["againPassword"]
        password = self.cleaned_data["password"]

        if againPassword != password:
            raise ValidationError("两次密码输入不一致，请重新输入！")

        return againPassword
