from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms import widgets as wid


class userLogin(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": wid.TextInput(attrs={'class': 'form-control'}),
            "password": wid.PasswordInput(attrs={'class': 'form-control'}),
        }