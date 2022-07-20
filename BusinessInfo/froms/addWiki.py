from django import forms
from BusinessInfo.models import wiki
from DevOps.froms import baseFroms

class addWikiFrom(baseFroms,forms.ModelForm):
    class Meta:
        model = wiki
        fields = ["fileType","name","pid"]