from django.shortcuts import render,get_object_or_404,render_to_response
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.conf import  settings
from . import models,forms
from django.contrib.auth.models import User
from .models import Asset

import uuid

import json,time,random
from django.utils.html import escape
# Create your views here.

def list(request):
    query_data=Asset.objects.all().values()
    return render_to_response("./asset/list.html", locals())

@login_required
@csrf_protect
def add(request):
    user = request.user
    error = ''
    if request.method == 'POST':
        form = forms.Asset_create_form(request.POST)
        if form.is_valid():
            asset_id = settings.VULN_PRE + str(uuid.uuid4())
            asset_name = form.cleaned_data['asset_name']
            asset_type = form.cleaned_data['asset_type']
            asset_key = form.cleaned_data['asset_key']
            asset_link = form.cleaned_data['asset_link']
            user_email = form.cleaned_data['user_email']
            asset_create = models.Asset.objects.get_or_create(
                asset_id=asset_id,
                asset_name=asset_name,
                asset_type=asset_type,
                asset_key=asset_key,
                asset_link=asset_link,
                )
            if asset_create[1]:
                asset = asset_create[0]
                if user.is_superuser:
                    asset.user_email = user_email
                    user_get = User.objects.filter(email = user_email).first()
                    if user_get:
                        asset.asset_inuse=True
                        asset.asset_user.add(user)
                    else:
                        asset.asset_inuse=False
                else:
                    asset.asset_inuse=True
                    if user_email:
                        asset.user_email = user_email
                    else:
                        asset.user_email = user.email
                    asset.asset_user.add(user)
                asset.save()
            error = '添加成功'
        else:
            error ='非法输入或资产已存在，请进行资产申请'
        return render(request,'./asset/add.html',{'form':form,'post_url':'add','error':error})
    else:
        form = forms.Asset_create_form()
    return render(request,'./asset/add.html',{'form':form,'post_url':'assetcreate'})
