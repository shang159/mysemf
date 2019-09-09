from . import models
from django import forms
from django.forms import ModelForm,widgets

class Asset_create_form(ModelForm):
    class Meta:
        model = models.Asset
        fields=['asset_name','asset_type','asset_key','asset_link','user_email']
        widgets ={
            'asset_name':widgets.TextInput(attrs={'class':'form-control','placeholder':'资产名称'}),
            'asset_type':widgets.Select(attrs={'class':'form-control','placeholder':'资产类型'}),
            'asset_key':widgets.TextInput(attrs={'class':'form-control','placeholder':'资产标识/服务器为ip，网站为域名或访问地址,APP为应用名称'}),
            'asset_link':widgets.Select(attrs={'class':'form-control','placeholder':'生产线'}),
            'user_email':widgets.TextInput(attrs={'class':'form-control','placeholder':'请填写资产使用者邮箱，默认为申请人员邮箱'}),
            }