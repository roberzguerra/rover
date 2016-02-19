# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_people', '0002_auto_20150820_0113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personcategory',
            options={'ordering': ('title',), 'verbose_name': 'Equipe', 'verbose_name_plural': 'Equipes'},
        ),
    ]
