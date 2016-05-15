# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('events', '0003_auto_20150820_0027'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', db_index=True, blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['status', 'pk'],
                'db_table': 'event_block',
                'verbose_name': 'Bloco para Evento',
                'verbose_name_plural': 'Blocos para Eventos',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='EventBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('link_menu', models.IntegerField(default=2, help_text='Se marcado exibe como link no menu principal.', verbose_name='Exibir no Menu', choices=[(2, 'Sim'), (1, 'N\xe3o')])),
                ('block', models.ForeignKey(blank=True, to='events.Block', help_text='Selecione o Evento deste Bloco.', null=True, verbose_name='Bloco')),
                ('event', models.ForeignKey(blank=True, to='events.Event', help_text='Selecione o Evento deste Bloco.', null=True, verbose_name='Evento')),
            ],
            options={
                'ordering': ['status', 'pk'],
                'db_table': 'event_eventblock',
                'verbose_name': 'Bloco de Evento',
                'verbose_name_plural': 'Blocos de Eventos',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='eventprogramation',
            name='event',
        ),
        migrations.DeleteModel(
            name='EventProgramation',
        ),
        migrations.RemoveField(
            model_name='event',
            name='information_active',
        ),
        migrations.RemoveField(
            model_name='event',
            name='information_text',
        ),
        migrations.RemoveField(
            model_name='event',
            name='information_title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='list_events_active',
        ),
        migrations.RemoveField(
            model_name='event',
            name='list_events_title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='list_programations_active',
        ),
        migrations.RemoveField(
            model_name='event',
            name='list_programations_title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='local_active',
        ),
        migrations.RemoveField(
            model_name='event',
            name='local_maps_name',
        ),
        migrations.RemoveField(
            model_name='event',
            name='local_text',
        ),
        migrations.RemoveField(
            model_name='event',
            name='local_title',
        ),
        migrations.RemoveField(
            model_name='event',
            name='observation_active',
        ),
        migrations.RemoveField(
            model_name='event',
            name='observation_text',
        ),
        migrations.RemoveField(
            model_name='event',
            name='observation_title',
        ),
    ]
