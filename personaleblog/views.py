# coding:utf-8
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage


# Create your views here.
def loginsafe(request):
    """
    1.首先判断是什么method
    2.如果是get,需要将模版返回，如果是Post则需要获取emailpassword 来认证
    3.如果认证失败，则判断
    """
    message = {'error': ''}
    if request.method == 'POST':
        eamil = request.POST['email']
        pwd = request.POST['password']
        user = authenticate(email=eamil, password=pwd)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
        else:
            message = {
                'error': '帐号或密码错误'
            }
    return render(request, "blog/login.html", message)


def logoutsafe(request):
    logout(request)
    return HttpResponseRedirect('/index/')


def register(request):
    if request.method == 'POST':
        pass

    return render(request, "")


def golob_setting(request):
    categroys = Category.objects.all()  # 把所有的分类给找出来
    tags = Tag.objects.all()
    archive = Article.objects.archive_distink()
    return {
        'categroys': categroys,
        'tags': tags,
        'archives': archive,
    }


# 这个是首页
def index(request):
    articles = Article.objects.filter(is_pass=True)  # 找出发布的文章
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    content = {
        'articles': articles,
        'current': 0,
    }
    return render(request, "blog/index.html", content)


# 查看详情
def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
        article.clicks += 1
        article.save()
    except Article.DoesNotExist:
        # 返回一个404页面
        pass
    return render(request, "blog/detail.html", {'article': article})


# 通过cartgory_name来获取文章信息，这里应该对nav进行activ处理
def category(request, category_name):
    try:
        category = Category.objects.get(slug=category_name)

    except Category.DoesNotExist:
        pass
    articles = Article.objects.filter(is_pass=True, categroy__name=category.name)  # 找出发布的文章
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    content = {
        'articles': articles,
        'current': category.id,
    }
    return render(request, "blog/index.html", content)


@login_required(login_url='/login/')
def comment(request):
    pass
