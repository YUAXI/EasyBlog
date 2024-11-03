from django.contrib import admin
from homeApp import models


class Server(admin.ModelAdmin):
    list_display = ('serverName', 'serverUrlLan', 'serverUrlFrp')
    # list_filter = ('published',)


class Project(admin.ModelAdmin):
    list_display = ('projectName', 'projectUrl')
    # list_filter = ('published',)


admin.site.register(models.SERVER, Server)
admin.site.register(models.PROJECT, Project)
admin.site.site_header = 'YUAXI\'Blog 管理后台'
