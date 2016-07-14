#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, name,password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,name='admin'):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

@python_2_unicode_compatible
class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    name=models.CharField(verbose_name='姓名',max_length=20,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name="用户"
        verbose_name_plural=verbose_name
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

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
    slug=models.SlugField(max_length=10,help_text="根据标签名字来获取url",unique=True)
    description=models.TextField('描述')
    create_at=models.DateField('创建时间',auto_now_add=True)
    update_at=models.DateField('更新时间',auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['create_at']
        verbose_name='标签'
        verbose_name_plural=verbose_name

    def get_absolute_url(self):
        return reverse('tag', args=[self.slug,])

class ArticleManage(models.Manager):
    def archive_distink(self):
        date_list=self.values('create_at')
        archive_list=[]
        for  date in date_list:
            date=date['create_at'].strftime("%Y/%m")
            if date not in archive_list:
                archive_list.append(date)
        return archive_list

@python_2_unicode_compatible
class Article(models.Model):
    title=models.CharField('标题',max_length=20,unique=True)
    content=RichTextField('正文')
    is_pass=models.BooleanField('是否发布',default=True)
    clicks=models.IntegerField(verbose_name='点击数',default=0)
    create_at=models.DateField('创建时间',auto_now_add=True)
    update_at=models.DateField('更新时间',auto_now=True)
    categroy=models.ForeignKey(Category,verbose_name='分类')
    tags=models.ManyToManyField(Tag,verbose_name='标签')

    objects=ArticleManage()
    def __str__(self):
        return self.title
    class Meta:
        ordering=['create_at']
        verbose_name='文章'
        verbose_name_plural=verbose_name
    def get_absolute_url(self):
        return reverse('article', args=[self.id, ])

