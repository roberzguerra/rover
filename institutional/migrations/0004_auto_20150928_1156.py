# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20150928_1038'),
        ('institutional', '0003_auto_20150928_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='slides',
        ),
        migrations.AddField(
            model_name='slide',
            name='page',
            field=models.ForeignKey(to='pages.Page', help_text='Project-Id-Version: Django\nReport-Msgid-Bugs-To: \nPOT-Creation-Date: 2013-05-02 16:18+0200\nPO-Revision-Date: 2010-05-13 15:35+0200\nLast-Translator: Django team\nLanguage-Team: English <en@li.org>\nLanguage: en\nMIME-Version: 1.0\nContent-Type: text/plain; charset=UTF-8\nContent-Transfer-Encoding: 8bit\n', null=True),
            preserve_default=True,
        ),
    ]
