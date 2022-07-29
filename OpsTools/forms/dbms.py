from django import forms
from OpsTools.models import dbms
from DevOps.forms import baseFroms

class addDatabaseInfoForm(baseFroms,forms.ModelForm):
    dbPasswd = forms.CharField(widget=forms.PasswordInput(),strip=True,
                               help_text='编辑时为空则不更改密码',label="数据库密码")
    class Meta:
        model = dbms
        fields = "__all__"
