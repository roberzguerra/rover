# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('mezzanine_file_collections', '0002_auto_20150928_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='_meta_title',
            field=models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='created',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='expiry_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='gen_description',
            field=models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='in_sitemap',
            field=models.BooleanField(default=True, verbose_name='Show in sitemap'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='keywords_string',
            field=models.CharField(max_length=500, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='publish_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', db_index=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='short_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='site',
            field=models.ForeignKey(default=1, editable=False, to='sites.Site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='slug',
            field=models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='status',
            field=models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mediafile',
            name='updated',
            field=models.DateTimeField(null=True, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mediafile',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Title'),
            preserve_default=True,
        ),
    ]
