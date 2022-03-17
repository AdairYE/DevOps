from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import widgets as wid


class userInfoForm(forms.ModelForm):
    againPasswd = fields.CharField(
        label="确认密码",
        widget=wid.PasswordInput(attrs={'class':'form-control'})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "againPasswd"]
        widgets = {
            "username": wid.TextInput(attrs={'class': 'form-control'}),
            "email": wid.EmailInput(attrs={'class': 'form-control'}),
            "password": wid.PasswordInput(attrs={'class': 'form-control'}),
        }
