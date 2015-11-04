# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0008_auto_20151014_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='url_access',
            field=models.CharField(default=1, help_text='Tipo de acesso \xe0 URL.', max_length=1, verbose_name='Tipo de Acesso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=mezzanine.core.fields.FileField(help_text='Envie imagens com resolu\xe7\xe3o de 1920x718px ou equivalente.', max_length=255, verbose_name='Imagem 1920x718px'),
            preserve_default=True,
        ),
    ]
