from django import forms
from DevOps.forms import baseFroms
from BusinessInfo.models import project

class addProjectFrom(baseFroms,forms.ModelForm):
    class Meta:
        model = project
        exclude = ["author","startDate","endDate","participator","starUsers"]