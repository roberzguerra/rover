# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_people', '0003_auto_20150928_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='_order',
            field=mezzanine.core.fields.OrderField(null=True, verbose_name='Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='mugshot',
            field=mezzanine.core.fields.FileField(help_text='Evie imagens com 182x182px.', max_length=255, null=True, verbose_name='Imagem de Perfil', blank=True),
            preserve_default=True,
        ),
    ]
