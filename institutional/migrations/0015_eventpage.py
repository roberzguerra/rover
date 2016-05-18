# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20151014_1122'),
        ('institutional', '0014_auto_20151014_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
                'db_table': 'institutional_event_page',
                'verbose_name': 'Lista de Eventos',
                'verbose_name_plural': 'Listas de Eventos',
            },
            bases=('pages.page', models.Model),
        ),
    ]
