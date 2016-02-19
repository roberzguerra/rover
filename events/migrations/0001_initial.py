# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.utils.models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
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
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('event_title_menu', models.CharField(help_text='T\xedtulo que vai no link \xe0 esquerda no Menu do Topo. M\xe1ximo 255 caracteres. Ex: Congresso', max_length=255, verbose_name='T\xedtulo do Evento para o Menu')),
                ('event_description_short', models.CharField(help_text='Descri\xe7\xe3o curta para Buscadores e Redes sociais. Ex: Congresso Escoteiro Regional 2015', max_length=255, verbose_name='Descri\xe7\xe3o curta')),
                ('event_logo', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Cabe\xe7alho Logo', blank=True)),
                ('event_title', mezzanine.core.fields.RichTextField(default=b'', help_text='This field can contain HTML and should contain a few paragraphs describing the background of the person.', verbose_name='Cabe\xe7alho T\xedtulo', blank=True)),
                ('event_image_background', mezzanine.core.fields.FileField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 2362x591px.', max_length=200, null=True, verbose_name='Cabe\xe7alho Imagem de Fundo', blank=True)),
                ('event_social_image', mezzanine.core.fields.FileField(help_text='Imagem para exibir em links de Redes Sociais, como Facebook. Para imagem retangular envie em 600x315, para imagem quadrada envie em 200x200. Ou formatos maiores sempre mantendo a propor\xe7\xe3o.', max_length=200, null=True, verbose_name='Imagem para Redes Sociais', blank=True)),
                ('information_active', models.IntegerField(default=0, verbose_name='Exibir Bloco Informa\xe7\xf5es', choices=[(1, 'Sim'), (0, 'N\xe3o')])),
                ('information_title', mezzanine.core.fields.RichTextField(null=True, verbose_name='Informa\xe7\xf5es T\xedtulo', blank=True)),
                ('information_text', mezzanine.core.fields.RichTextField(null=True, verbose_name='Informa\xe7\xf5es Texto', blank=True)),
                ('local_active', models.IntegerField(default=0, verbose_name='Exibir Bloco Local', choices=[(1, 'Sim'), (0, 'N\xe3o')])),
                ('local_maps_name', models.CharField(help_text='Nome do Local no Google Maps.', max_length=500, verbose_name='Local no Maps', blank=True)),
                ('local_title', mezzanine.core.fields.RichTextField(null=True, verbose_name='Local T\xedtulo', blank=True)),
                ('local_text', mezzanine.core.fields.RichTextField(verbose_name='Local Texto', blank=True)),
                ('observation_active', models.IntegerField(default=0, verbose_name='Exibir Bloco Observa\xe7\xf5es', choices=[(1, 'Sim'), (0, 'N\xe3o')])),
                ('observation_title', mezzanine.core.fields.RichTextField(null=True, verbose_name='Observa\xe7\xf5es T\xedtulo', blank=True)),
                ('observation_text', mezzanine.core.fields.RichTextField(verbose_name='Observa\xe7\xf5es Texto', blank=True)),
                ('list_programations_active', models.IntegerField(default=0, max_length=1, verbose_name='Ativar Lista de Programa\xe7\xf5es', choices=[(1, 'Sim'), (0, 'N\xe3o')])),
                ('list_programations_title', mezzanine.core.fields.RichTextField(verbose_name='Lista de Programa\xe7\xf5es T\xedtulo', blank=True)),
                ('list_events_active', models.IntegerField(default=0, max_length=1, verbose_name='Ativar Lista de Eventos', choices=[(1, 'Sim'), (0, 'N\xe3o')])),
                ('list_events_title', mezzanine.core.fields.RichTextField(null=True, verbose_name='Lista de Eventos T\xedtulo', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['status', 'pk'],
                'db_table': 'event_homepage',
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='EventProgramation',
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
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', mezzanine.core.fields.FileField(help_text='Para n\xe3o distorcer, envie uma imagem com resolu\xe7\xe3o m\xe1xima de 200x200px.', max_length=200, null=True, verbose_name='Imagem', blank=True)),
                ('date_time', models.DateTimeField(verbose_name='Data e Hora')),
                ('event', models.ForeignKey(blank=True, to='events.Event', help_text='Selecione o Evento desta Programa\xe7\xe3o.', null=True, verbose_name='Evento')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['-name', '-description'],
                'db_table': 'event_programation',
                'verbose_name': 'Programa\xe7\xe3o',
                'verbose_name_plural': 'Programa\xe7\xf5es',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
    ]
