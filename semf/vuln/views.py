#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
import time,json
import uuid
from . import models,forms
# Create your views here.
# Create your views here.
@login_required
def list(request):
    return render(request,"./vuln/list.html")





VULN_LEAVE={
    '0':'信息',
    '1':'低危',
    '2':'中危',
    '3':'高危',
    '4':'紧急'
    }
VULN_STATUS={
    '0':'已忽略',
    '1':'已修复',
    '2':'待修复',
    '3':'漏洞重现',
    '4':'复查中',
    }




@login_required
@csrf_protect
def vuln_change_status(request,vuln_id):
    user = request.user
    error=''
    if user.is_superuser:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_id=vuln_id)
    else:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_asset__asset_user=user,vuln_id=vuln_id)
    if vuln:
        if request.method == 'POST':
            form = forms.Vuln_action_form(request.POST,instance=vuln)
            if form.is_valid():
                form.save()
                error = '更改成功'
            else:
                error = '请检查参数'
        else:
            form = forms.Vuln_action_form(instance=vuln)
    else:
        error ='请检查参数'
    return render(request,'formupdate.html',{'form':form,'post_url':'vulnfix','argu':vuln_id,'error':error})




@login_required
@csrf_protect
def vuln_update(request,vuln_id):
    user = request.user
    error=''
    if user.is_superuser:
        vuln = get_object_or_404(models.Vulnerability_scan,vuln_id=vuln_id)
        if vuln:
            if request.method == 'POST':
                form = forms.Vuln_edit_form(request.POST,instance=vuln)
                if form.is_valid():
                    form.save()
                    error = '更改成功'
                else:
                    error = '请检查参数'
            else:
                form = forms.Vuln_edit_form(instance=vuln)
        else:
            error ='请检查参数'
    else:
        error = '权限错误'
    return render(request,'formupdate.html',{'form':form,'post_url':'vulnupdate','argu':vuln_id,'error':error})


@login_required
@csrf_protect
def add(request,asset_id):
    user = request.user
    error =''
    if user.is_superuser:
        asset = get_object_or_404(models.Asset,asset_id=asset_id)
    else:
        asset = get_object_or_404(models.Asset,asset_user = user,asset_id=asset_id)
    if request.method == 'POST':
        form = forms.Vuln_edit_form(request.POST)
        if form.is_valid():
            try:
                num = models.Vulnerability.objects.latest('id').id
            except Exception:
                num = 0
            num =num+1
            vuln_name = form.cleaned_data['vuln_name']
            leave = form.cleaned_data['leave']
            introduce = form.cleaned_data['introduce']
            vuln_info = form.cleaned_data['vuln_info']
            scopen = form.cleaned_data['scopen']
            fix = form.cleaned_data['fix']
            vuln_id = "Vuln-" + str(uuid.uuid4())
            res=models.Vulnerability.objects.get_or_create(
                                                                vuln_name=vuln_name,
                                                                 leave=leave,
                                                                scopen=scopen,
                                                                 introduce=introduce,
                                                                 vuln_info=vuln_info,
                                                                fix=fix,

                                                                 )
            vuln = res[0]
            if vuln.vuln_id == vuln_id:
                if vuln.fix_status == '1':
                    vuln.fix_status= '3'
            else:
                vuln.vuln_id = vuln_id
                if leave == '0':
                    vuln.fix_status= '0'
                vuln.fix_status= '2'
            vuln.save()
            error='添加成功'
        else:
            error = '请检查输入'
    else:
        form = forms.Vuln_edit_form()
    return render(request,'formupdate.html',{'form':form,'post_url':'vulncreate','argu':asset_id,'error':error})