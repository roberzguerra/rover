# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150527_1555'),
        ('sites', '0001_initial'),
        ('pages', '0006_auto_20150928_1038'),
        ('institutional', '0002_auto_20150915_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('blog_posts', models.ManyToManyField(help_text='Not\xedcias para exibir em destaque na p\xe1gina.', to='blog.BlogPost', verbose_name='Not\xedcias em Destaque')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('image', mezzanine.core.fields.FileField(help_text='Envie imagens com resolu\xe7\xe3o de 1920x718px     ou equivalente.', max_length=255, verbose_name='Imagem')),
                ('description', models.CharField(help_text='Descri\xe7\xe3o', max_length=500, verbose_name='Descri\xe7\xe3o', blank=True)),
                ('caption', models.CharField(max_length=500, verbose_name='Caption', blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            options={
                'ordering': ['_order'],
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='homepage',
            name='slides',
            field=models.ManyToManyField(to='institutional.Slide', verbose_name='Slides em Destaque'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='homepage',
            name='teams',
            field=models.ManyToManyField(help_text='Equipes em destaque para exibir na p\xe1gina.', to='institutional.Team', verbose_name='Equipes em Destaque'),
            preserve_default=True,
        ),
    ]
