from django.db import models


# Create your models here.
class SERVER(models.Model):
    serverName = models.CharField(
        max_length=10,
        verbose_name='服务名称',
        null=False,
    )
    serverUrlLan = models.URLField(
        verbose_name='服务器内网IPv4地址',
        null=False
    )
    serverUrlFrp = models.URLField(
        verbose_name='服务器穿透址',
        null=True,
        blank=True
    )
    serverUrlWan = models.URLField(
        verbose_name='服务器公网IPv4地址',
        null=True,
        blank=True
    )
    serverUrlWan6 = models.URLField(
        verbose_name='服务器公网IPv6地址',
        null=True,
        blank=True
    )
    serverImg = models.ImageField(
        verbose_name='服务标',
        null=False,
        upload_to='serverImg/'
    )

    class Meta:
        verbose_name = '服务'
        verbose_name_plural = verbose_name


class PROJECT(models.Model):
    projectName = models.CharField(
        max_length=10,
        verbose_name='项目名称',
        null=False
    )
    projectUrl = models.URLField(
        verbose_name='项目地址',
        null=True
    )
    projectDetail = models.TextField(
        verbose_name='项目介绍',
        null=True
    )
    projectImg = models.ImageField(
        verbose_name='项目图片',
        null=False,
        upload_to='projectImg/'
    )

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name
