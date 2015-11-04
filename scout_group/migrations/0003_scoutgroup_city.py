# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scout_group', '0002_auto_20150915_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoutgroup',
            name='city',
            field=models.CharField(max_length=500, verbose_name='cidade', blank=True),
            preserve_default=True,
        ),
    ]
