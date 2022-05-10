from django import forms
from BusinessInfo.models import product
from DevOps.froms import baseFroms

class addProductFrom(baseFroms,forms.ModelForm):
    class Meta:
        model = product
        fields = ["name", "code", "explain"]