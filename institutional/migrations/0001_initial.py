# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('mezzanine_people', '0002_auto_20150820_0113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('categories', models.ManyToManyField(help_text='Selecione as equipes para exibir na p\xe1gina.', related_name='people_category', verbose_name='Equipes', to='mezzanine_people.PersonCategory', blank=True)),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
            bases=('pages.page', models.Model),
        ),
    ]
