# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0009_auto_20151014_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='url_access',
            field=models.CharField(default=1, help_text='Tipo de acesso \xe0 URL.', max_length=1, verbose_name='Tipo de Acesso', choices=[(b'1', 'Mesma Janela/Aba'), (b'2', 'Nova Janela/Aba')]),
            preserve_default=True,
        ),
    ]
