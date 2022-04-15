from django import forms
from BusinessInfo.models import project
from DevOps.froms import baseFroms

class editProjectFrom(baseFroms,forms.ModelForm):
    class Meta:
        model = project
        fields = "__all__"