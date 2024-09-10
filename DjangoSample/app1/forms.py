from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.Form):
    # ModelChoiceField is used to query a particular model
    # choiceField is a dropdown
    chai_variety = forms.ModelChoiceField(queryset=ChaiVariety.objects.all(), label='select chai variety')
    # we get only names in chai_variety from ChaiVariety model because in that model - we have returned only name in __str__ function