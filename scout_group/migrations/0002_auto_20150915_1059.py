# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scout_group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoutgroup',
            name='district',
            field=models.ForeignKey(verbose_name='Distrito', to='scout_group.District'),
            preserve_default=True,
        ),
    ]
