# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150915_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=mezzanine.core.fields.FileField(help_text='Propor\xe7\xe3o 1920x300px.', max_length=255, verbose_name='Imagem de Destaque', blank=True),
            preserve_default=True,
        ),
    ]
