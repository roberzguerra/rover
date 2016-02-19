# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0011_auto_20151014_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='blog_posts',
            field=models.ManyToManyField(help_text='Not\xedcias para exibir em destaque na p\xe1gina.', to='blog.BlogPost', null=True, verbose_name='Not\xedcias em Destaque', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='homepage',
            name='teams',
            field=models.ManyToManyField(help_text='Equipes em destaque para exibir na p\xe1gina.', to='mezzanine_people.PersonCategory', null=True, verbose_name='Equipes em Destaque', blank=True),
            preserve_default=True,
        ),
    ]
