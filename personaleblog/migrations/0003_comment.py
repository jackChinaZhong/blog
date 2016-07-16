# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('personaleblog', '0002_auto_20160712_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='\u8bc4\u8bba\u65e5\u671f')),
                ('content', models.CharField(max_length=300, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
                ('article', models.ForeignKey(verbose_name='\u6587\u7ae0', to='personaleblog.Article')),
                ('comment_parent', models.ForeignKey(verbose_name='\u7236\u7ea7\u8bc4\u8bba', blank=True, to='personaleblog.Comment', null=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id', 'date'],
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
        ),
    ]
