from django import forms
from BusinessInfo.models import product
from DevOps.forms import baseFroms

class addProductForm(baseFroms,forms.ModelForm):
    class Meta:
        model = product
        fields = ["name", "code", "explain"]