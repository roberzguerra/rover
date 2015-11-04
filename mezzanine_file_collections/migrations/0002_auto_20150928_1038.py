# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_file_collections', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mediafile',
            options={'ordering': ('_order',), 'verbose_name': 'Arquivo', 'verbose_name_plural': 'Arquivos'},
        ),
        migrations.AlterModelOptions(
            name='medialibrary',
            options={'ordering': ('_order',), 'verbose_name': 'Download', 'verbose_name_plural': 'Downloads'},
        ),
    ]
