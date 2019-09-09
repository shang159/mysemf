from . import models
from django.forms import ModelForm,widgets

class Vuln_edit_form(ModelForm):
    class Meta:
        model = models.Vulnerability
        fields = ['vuln_name','leave','scopen','introduce','fix']
        widgets = {
                   'vuln_name':widgets.TextInput(attrs={'class':'form-control','placeholder':'漏洞名称'}),
                   'leave':widgets.Select(attrs={'class':'form-control','placeholder':'危险等级'}),
                   'scopen':widgets.TextInput(attrs={'class':'form-control','placeholder':'影响范围'}),
                   'introduce':widgets.Textarea(attrs={'class':'form-control','placeholder':'漏洞介绍','style':'height:100px'}),
                   'fix':widgets.Textarea(attrs={'class':'form-control','placeholder':'修复方案','style':'height:100px'}),
        }