from json import JSONDecodeError
from django.shortcuts import render
from .models import *
import requests
import json


def home(request):
    # 获取每日一言
    try:
        response = requests.get('https://v1.hitokoto.cn/')
        json_content = json.loads(response.text)
        text = '「'+json_content['hitokoto']+'」'
    except JSONDecodeError:
        text = ""
        print("请求失败")
    servers = SERVER.objects.all()
    projects = PROJECT.objects.all()
    return render(request, 'index.html', {
        "text": text,
        "servers": servers,
        "projects": projects
    })
