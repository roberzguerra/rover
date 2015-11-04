# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150812_1618'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventprogramation',
            options={'ordering': ['-date_time', '-name'], 'verbose_name': 'Programa\xe7\xe3o', 'verbose_name_plural': 'Programa\xe7\xf5es'},
        ),
        migrations.AlterField(
            model_name='event',
            name='information_active',
            field=models.IntegerField(default=1, verbose_name='Exibir Bloco Informa\xe7\xf5es', choices=[(2, 'Sim'), (1, 'N\xe3o')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='list_events_active',
            field=models.IntegerField(default=1, max_length=1, verbose_name='Ativar Lista de Eventos', choices=[(2, 'Sim'), (1, 'N\xe3o')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='list_programations_active',
            field=models.IntegerField(default=1, max_length=1, verbose_name='Ativar Lista de Programa\xe7\xf5es', choices=[(2, 'Sim'), (1, 'N\xe3o')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='local_active',
            field=models.IntegerField(default=1, verbose_name='Exibir Bloco Local', choices=[(2, 'Sim'), (1, 'N\xe3o')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='observation_active',
            field=models.IntegerField(default=1, verbose_name='Exibir Bloco Observa\xe7\xf5es', choices=[(2, 'Sim'), (1, 'N\xe3o')]),
            preserve_default=True,
        ),
    ]
