from django.db import models


class Vulnerability(models.Model):
    vuln_id = models.CharField('漏洞编号',max_length=30)
    vuln_name = models.CharField('漏洞名称', max_length=255)
    leave = models.CharField('危险等级',max_length=10)
    scopen = models.TextField('影响范围',null=True,blank=True)
    introduce = models.TextField('漏洞简介',null=True,blank=True)
    fix = models.TextField('修复方案',null=True,blank=True)
    update_data = models.DateTimeField("更新日期",auto_now=True)
    def __str__(self):
        return self.vuln_id
