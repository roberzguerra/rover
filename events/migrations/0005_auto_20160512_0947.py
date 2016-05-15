# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('events', '0004_auto_20160510_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventProgramation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('link_menu', models.IntegerField(default=2, help_text='Se marcado exibe como link no menu principal.', verbose_name='Exibir no Menu', choices=[(2, 'Sim'), (1, 'N\xe3o')])),
                ('event', models.ForeignKey(blank=True, to='events.Event', help_text='Selecione o Evento deste Bloco.', null=True, verbose_name='Evento')),
            ],
            options={
                'ordering': ['status', 'pk'],
                'db_table': 'event_eventprogramation',
                'verbose_name': 'Bloco de Evento',
                'verbose_name_plural': 'Blocos de Eventos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Programation',
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
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', mezzanine.core.fields.FileField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200x200px.', max_length=200, null=True, verbose_name='Imagem', blank=True)),
                ('date_time', models.DateTimeField(verbose_name='Data e Hora')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['-date_time', '-name'],
                'db_table': 'event_programation',
                'verbose_name': 'Programa\xe7\xe3o',
                'verbose_name_plural': 'Programa\xe7\xf5es',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.AddField(
            model_name='eventprogramation',
            name='programation',
            field=models.ForeignKey(blank=True, to='events.Programation', help_text='Selecione a Programa\xe7\xe3o deste Bloco.', null=True, verbose_name='Programa\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.TextField(help_text='Insira aqui c\xf3digos HTML, CSS ou JS.', null=True, verbose_name='C\xf3digos', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='eventblock',
            name='type',
            field=models.IntegerField(default=1, help_text='Selecione Programa\xe7\xe3o para exibir as programa\xe7\xf5es do evento.', verbose_name='Tipo', choices=[(1, 'Conte\xfado'), (2, 'Programa\xe7\xe3o')]),
            preserve_default=True,
        ),
    ]
