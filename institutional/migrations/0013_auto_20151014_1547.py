# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institutional', '0012_auto_20151014_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=mezzanine.core.fields.FileField(help_text='Envie imagens com resolu\xe7\xe3o de 1920x718px ou equivalente.', max_length=255, null=True, verbose_name='Imagem 1920x718px', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='page',
            field=models.ForeignKey(blank=True, to='pages.Page', help_text='Project-Id-Version: Django\nReport-Msgid-Bugs-To: \nPOT-Creation-Date: 2013-05-02 16:18+0200\nPO-Revision-Date: 2010-05-13 15:35+0200\nLast-Translator: Django team\nLanguage-Team: English <en@li.org>\nLanguage: en\nMIME-Version: 1.0\nContent-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='slide',
            name='url_access',
            field=models.CharField(default=1, choices=[(b'1', 'Mesma Janela/Aba'), (b'2', 'Nova Janela/Aba')], max_length=1, blank=True, help_text='Tipo de acesso \xe0 URL.', verbose_name='Tipo de Acesso'),
            preserve_default=True,
        ),
    ]
