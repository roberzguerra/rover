# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_page_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=mezzanine.core.fields.FileField(max_length=255, verbose_name='Imagem de Destaque, propor\xe7\xe3o 1920', blank=True),
            preserve_default=True,
        ),
    ]
