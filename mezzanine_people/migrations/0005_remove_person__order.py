# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_people', '0004_auto_20151019_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='_order',
        ),
    ]
