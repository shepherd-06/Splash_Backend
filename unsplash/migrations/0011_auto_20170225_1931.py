# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-25 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unsplash', '0010_auto_20170225_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='exif_make',
            field=models.CharField(blank=True, default='none', max_length=50, null=True),
        ),
    ]