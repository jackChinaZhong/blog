#coding:utf-8
from django.shortcuts import render,HttpResponse
import logging
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    pass
def logout(request):
    pass

def golob_setting(request):
    categroys = Category.objects.all()  # 把所有的分类给找出来
    return {
        'categroys':categroys,
     }
#这个是首页
def index(request):
    articles=Article.objects.filter(is_pass=True)#找出发布的文章
    content={
        'articles':articles,
    }
    return render(request, "blog/index.html", content)

#查看详情
def detail(request,article_id):
    try:
        article=Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        pass
    return render(request, "blog/detail.html",{'article':article})
#通过cartgory_name来获取文章信息，这里应该对nav进行activ处理
def category(request,categroy_name):
    articles = Article.objects.filter(is_pass=True,categroy__name=categroy_name)  # 找出发布的文章
    content={
        'articles':articles,
    }
    return render(request,"blog/detail.html",content)