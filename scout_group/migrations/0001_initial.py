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
            name='District',
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
                ('name', models.CharField(max_length=500, verbose_name='Nome')),
                ('number', models.IntegerField(verbose_name='Numeral')),
                ('logo', mezzanine.core.fields.FileField(help_text='Envie imagens com propor\xe7\xe3o de 140x140px', max_length=255, null=True, verbose_name='Logo', blank=True)),
                ('coordinator_name', models.CharField(max_length=255, verbose_name='Coordenador Distrital')),
                ('email', models.EmailField(help_text='E-mail do distrito ou do coordenador.', max_length=255, blank=True)),
                ('uf', models.CharField(default=b'RS', help_text='Estado do Distrito.', max_length=2, verbose_name='UF', choices=[(b'RS', 'Rio Grande do Sul'), (b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AP', 'Amap\xe1'), (b'AM', 'Amazonas'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MT', 'Mato Grosso'), (b'MS', 'Mato Grosso do Sul'), (b'MG', 'Minas Gerais'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PR', 'Paran\xe1'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'SC', 'Santa Catarina'), (b'SP', 'S\xe3o Paulo'), (b'SE', 'Sergipe'), (b'TO', 'Tocantins')])),
                ('address', models.CharField(max_length=500, verbose_name='Endere\xe7o', blank=True)),
                ('cep', models.CharField(max_length=8, verbose_name='CEP', blank=True)),
                ('image', mezzanine.core.fields.FileField(help_text='Imagem do topo da p\xe1gina, com propor\xe7\xe3o de 1920x300px', max_length=255, null=True, verbose_name='Imagem Destaque', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['number', 'name'],
                'db_table': 'scout_group_district',
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='ScoutGroup',
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
                ('name', models.CharField(max_length=500, verbose_name='Nome')),
                ('number', models.IntegerField(verbose_name='Numeral')),
                ('logo', mezzanine.core.fields.FileField(help_text='Envie uma imagem com propor\xe7\xe3o de 140x140px', max_length=255, null=True, verbose_name='Logo do Grupo', blank=True)),
                ('uf', models.CharField(default=b'RS', help_text='Estado do Grupo Escoteiro.', max_length=2, verbose_name='UF', choices=[(b'RS', 'Rio Grande do Sul'), (b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AP', 'Amap\xe1'), (b'AM', 'Amazonas'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MT', 'Mato Grosso'), (b'MS', 'Mato Grosso do Sul'), (b'MG', 'Minas Gerais'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PR', 'Paran\xe1'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'SC', 'Santa Catarina'), (b'SP', 'S\xe3o Paulo'), (b'SE', 'Sergipe'), (b'TO', 'Tocantins')])),
                ('address', models.CharField(max_length=500, verbose_name='Endere\xe7o', blank=True)),
                ('cep', models.CharField(max_length=8, verbose_name='CEP', blank=True)),
                ('email', models.EmailField(max_length=255, blank=True)),
                ('president_name', models.CharField(max_length=255, verbose_name='Presidente')),
                ('image', mezzanine.core.fields.FileField(help_text='Imagem do topo da p\xe1gina, propor\xe7\xe3o de 1920x300px', max_length=255, null=True, verbose_name='Imagem Destaque', blank=True)),
                ('district', models.ForeignKey(to='scout_group.District')),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'ordering': ['number', 'name'],
                'db_table': 'scout_group',
                'verbose_name': 'Grupo Escoteiro',
                'verbose_name_plural': 'Grupos Escoteiros',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
    ]
