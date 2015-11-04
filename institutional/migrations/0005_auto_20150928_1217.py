# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0004_auto_20150928_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='site',
        ),
        migrations.AddField(
            model_name='slide',
            name='url',
            field=models.CharField(help_text='Cole aqui a URL de destino do link.', max_length=500, verbose_name='URL', blank=True),
            preserve_default=True,
        ),
    ]
