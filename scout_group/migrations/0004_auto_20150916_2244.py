# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scout_group', '0003_scoutgroup_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoutgroup',
            name='logo',
            field=mezzanine.core.fields.FileField(help_text='Envie uma imagem com propor\xe7\xe3o de 182x182px', max_length=255, null=True, verbose_name='Logo do Grupo', blank=True),
            preserve_default=True,
        ),
    ]
