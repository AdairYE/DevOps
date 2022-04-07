from django import forms
from WorkOrder.models import product
from DevOps.froms import baseFroms

class editProductFrom(baseFroms,forms.ModelForm):
    class Meta:
        model = product
        fields = ["name", "code", "productOwner", "explain"]