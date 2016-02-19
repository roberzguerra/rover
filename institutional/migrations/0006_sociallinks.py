# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0005_auto_20150928_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('type', models.CharField(max_length=1, verbose_name='Tipo', choices=[(b'1', 'Facebook'), (b'2', 'Youtube'), (b'3', 'Twitter')])),
                ('url', models.URLField(help_text='Link da Rede Social', max_length=500, verbose_name='Url')),
                ('page', models.ForeignKey(to='institutional.HomePage')),
            ],
            options={
                'ordering': ['type', 'url'],
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
            bases=(models.Model,),
        ),
    ]
