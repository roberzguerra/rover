# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventprogramation',
            options={'ordering': ['-name', '-date_time'], 'verbose_name': 'Programa\xe7\xe3o', 'verbose_name_plural': 'Programa\xe7\xf5es'},
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='_meta_title',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='created',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='description',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='gen_description',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='in_sitemap',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='keywords_string',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='short_url',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='site',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='title',
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='updated',
        ),
        migrations.AlterField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', db_index=True, blank=True),
            preserve_default=True,
        ),
    ]
