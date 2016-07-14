# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email\u5730\u5740')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=20, verbose_name='\u6807\u9898')),
                ('content', ckeditor.fields.RichTextField(verbose_name='\u6b63\u6587')),
                ('is_pass', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('clicks', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='\u5206\u7c7b')),
                ('slug', models.SlugField(help_text='\u6839\u636e\u540d\u79f0\u6765\u521b\u5efaurl', unique=True, max_length=20)),
                ('describe', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
                'permissions': (('can_see', 'Can see view'), ('can_add', 'Can add view')),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='\u6807\u7b7e\u540d\u79f0')),
                ('slug', models.SlugField(help_text='\u6839\u636e\u6807\u7b7e\u540d\u5b57\u6765\u83b7\u53d6url', unique=True, max_length=10)),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('create_at', models.DateField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_at', models.DateField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['create_at'],
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='categroy',
            field=models.ForeignKey(verbose_name='\u5206\u7c7b', to='personaleblog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='personaleblog.Tag', verbose_name='\u6807\u7b7e'),
        ),
    ]
