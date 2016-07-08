#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

# Create your models here.
@python_2_unicode_compatible
class Category(models.Model):
    name=models.CharField('分类',max_length=20,unique=True)
    slug=models.SlugField(max_length=20,help_text='根据名称来创建url',unique=True)
    describe=models.TextField('描述')
    create_at=models.DateField('创建时间',auto_now_add=True)
    update_at=models.DateField('更新时间',auto_now=True)

    def get_absolute_url(self):
        return reverse('category',args=[self.slug,])
    def __str__(self):
        return self.name
    class Meta:
        ordering=['create_at']
        verbose_name='分类'
        verbose_name_plural=verbose_name
        permissions=(
            ('can_see','Can see view'),
            ('can_add','Can add view'),
        )

@python_2_unicode_compatible
class Tag(models.Model):
    name=models.CharField('标签名称',max_length=20,unique=True)
    description=models.TextField('描述')
    create_at=models.DateField('创建时间',auto_now_add=True)
    update_at=models.DateField('更新时间',auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['create_at']
        verbose_name='标签'
        verbose_name_plural=verbose_name


@python_2_unicode_compatible
class Article(models.Model):
    title=models.CharField('标题',max_length=20,unique=True)
    content=models.TextField(verbose_name='正文')
    is_pass=models.BooleanField('是否发布',default=True)
    clicks=models.IntegerField(verbose_name='点击数',default=0)

    create_at=models.DateField('创建时间',auto_now_add=True)
    update_at=models.DateField('更新时间',auto_now=True)
    categroy=models.ForeignKey(Category,verbose_name='分类')
    tags=models.ManyToManyField(Tag,verbose_name='标签')
    def __str__(self):
        return self.title
    class Meta:
        ordering=['create_at']
    def get_absolute_url(self):
        return reverse('article', args=[self.id, ])

