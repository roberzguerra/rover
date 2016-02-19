# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0006_sociallinks'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'ordering': ('_order',), 'verbose_name': 'P\xe1gina Inicial', 'verbose_name_plural': 'P\xe1ginas Iniciais'},
        ),
    ]
