from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import widgets as wid
from django.core.exceptions import ValidationError


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

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs["placeholder"] = "请输入{}".format(field.label)