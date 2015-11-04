# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0007_auto_20151007_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=mezzanine.core.fields.FileField(help_text='Envie imagens com resolu\xe7\xe3o de 1920x718px ou equivalente.', max_length=255, verbose_name='Imagem'),
            preserve_default=True,
        ),
    ]
