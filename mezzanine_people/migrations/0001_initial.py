# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
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
                ('first_name', models.CharField(max_length=100, verbose_name='Primeiro Nome', blank=True)),
                ('last_name', models.CharField(max_length=100, verbose_name='\xdaltimo Nome', blank=True)),
                ('mugshot', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Imagem de Perfil', blank=True)),
                ('mugshot_credit', models.CharField(max_length=200, verbose_name='Imagem de Perfil (credit)', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='E-mail', blank=True)),
                ('bio', mezzanine.core.fields.RichTextField(default=b'', help_text='Breve biografia da pessoa e/ou cargo.', verbose_name='Biografia', blank=True)),
                ('job_title', models.CharField(help_text='Exemplo: Diretor Presidente', max_length=60, verbose_name='T\xedtulo do Cargo', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Ordem')),
            ],
            options={
                'ordering': ('order', 'last_name', 'first_name'),
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Equipe',
                'verbose_name_plural': 'Equipes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Nome do link, ex: Twitter, Facebook...', max_length=50, verbose_name='Nome do Link')),
                ('url', models.URLField(verbose_name='URL')),
                ('person', models.ForeignKey(to='mezzanine_people.Person')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Link da Pessoa',
                'verbose_name_plural': 'Links da Pessoa',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='categories',
            field=models.ManyToManyField(related_name='people', verbose_name='Equipes', to='mezzanine_people.PersonCategory', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='site',
            field=models.ForeignKey(editable=False, to='sites.Site'),
            preserve_default=True,
        ),
    ]
