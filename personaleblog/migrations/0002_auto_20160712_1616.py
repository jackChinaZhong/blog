# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('personaleblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 7, 12, 8, 16, 24, 288000, tzinfo=utc), unique=True, max_length=20, verbose_name='\u59d3\u540d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='email'),
        ),
    ]
