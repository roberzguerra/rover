# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=mezzanine.core.fields.FileField(max_length=255, verbose_name='Imagem de Destaque', blank=True),
            preserve_default=True,
        ),
    ]
