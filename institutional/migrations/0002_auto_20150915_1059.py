# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20150915_0009'),
        ('institutional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScoutGroupPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('type', models.IntegerField(help_text='Tipo de exibi\xe7\xe3o dos itens da p\xe1gina', max_length=2, verbose_name='Tipo de Exibi\xe7\xe3o', choices=[(1, 'Grupos em ordem Alfab\xe9tica'), (2, 'Grupos por N\xfameral'), (3, 'Grupos por Distritos'), (4, 'Somente Distritos')])),
            ],
            options={
                'ordering': ('_order',),
                'db_table': 'institutional_scout_group_page',
                'verbose_name': 'Grupo | Distrito',
                'verbose_name_plural': 'Grupos | Distritos',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AlterModelTable(
            name='team',
            table='institutional_team',
        ),
    ]
