from django import forms
from DevOps.froms import baseFroms
from BusinessInfo.models import project

class addProjectFrom(baseFroms,forms.ModelForm):
    class Meta:
        model = project
        exclude = ["author","star"]