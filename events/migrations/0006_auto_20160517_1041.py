# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20160512_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventprogramation',
            options={'ordering': ['status', 'pk'], 'verbose_name': 'Programa\xe7\xe3o', 'verbose_name_plural': 'Programa\xe7\xf5es'},
        ),
        migrations.AlterField(
            model_name='programation',
            name='date_time',
            field=models.DateTimeField(help_text='Data e hora da realiza\xe7\xe3o do programa.', verbose_name='Data e Hora'),
            preserve_default=True,
        ),
    ]
