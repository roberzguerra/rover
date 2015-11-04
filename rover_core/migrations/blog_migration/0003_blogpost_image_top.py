# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser_safe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image_top',
            field=filebrowser_safe.fields.FileBrowseField(help_text='Imagem do topo da not\xedcia, resolu\xe7\xe3o m\xednima 1920x300px ou proporcional.', max_length=255, null=True, verbose_name='Imagem destaque topo', blank=True),
            preserve_default=True,
        ),
    ]
