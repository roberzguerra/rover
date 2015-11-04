# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filebrowser_safe.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150928_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=filebrowser_safe.fields.FileBrowseField(help_text='Propor\xe7\xe3o 1920x300px.', max_length=255, verbose_name='Imagem Destaque', blank=True),
            preserve_default=True,
        ),
    ]
