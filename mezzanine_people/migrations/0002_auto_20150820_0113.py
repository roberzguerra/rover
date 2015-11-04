# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('mezzanine_people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personcategory',
            name='site',
            field=models.ForeignKey(default='', editable=False, to='sites.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personcategory',
            name='slug',
            field=models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personcategory',
            name='title',
            field=models.CharField(default='', max_length=500, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
