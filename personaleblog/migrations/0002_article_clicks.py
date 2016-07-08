# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personaleblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='clicks',
            field=models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u6570'),
        ),
    ]
